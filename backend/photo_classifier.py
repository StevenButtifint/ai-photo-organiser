import timm
import torch
import json
from PIL import Image
import torchvision.transforms as transforms

from constants import CLASSES_DIR, MODEL


class PhotoClassifier:
    def __init__(self):
        self.model = None
        self.class_index = None
        self.model_loaded = False

    def setup_model(self):
        state_message = ""
        try:
            self.model = timm.create_model(MODEL, pretrained=True)
            self.model.eval()
            self.model_loaded = True
            state, state_message = self.load_classes()
        except timm.models.model_names:
            state = 500
        except timm.pretrained_weights:
            state = 501
        except FileNotFoundError:
            state = 502
        except Exception as e:
            state = 900
            state_message = str(e)
        return state, state_message

    def is_model_loaded(self):
        return self.model_loaded

    def load_classes(self):
        try:
            with open(CLASSES_DIR, 'r') as file:
                self.class_index = json.load(file)
            return 200, ""
        except FileNotFoundError:
            return 502, ""
        except Exception as e:
            return 900, str(e)

    @staticmethod
    def preprocess_photo(photo_path):
        photo = Image.open(photo_path)
        preprocessed_photo = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        return preprocessed_photo(photo)

    def classify_photo(self, preprocessed_photo):
        with torch.no_grad():
            output = self.model(preprocessed_photo.unsqueeze(0))
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        predicted_class = torch.argmax(probabilities).item()
        predicted_label = self.class_index.get(str(predicted_class))[1]
        return predicted_label
