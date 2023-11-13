import timm
import torch
import json
from PIL import Image
import torchvision.transforms as transforms


class PhotoClassifier:
    def __init__(self):
        self.model = None
        self.class_index = None
        self.model_loaded = False

    def setup_model(self):
        try:
            self.model = timm.create_model('efficientnet_b3', pretrained=True)
            self.model.eval()
            self.model_loaded = True
            self.load_classes()
            state = 200
        except timm.models.model_names:
            state = 500
        except timm.pretrained_weights:
            state = 501
        except Exception as e:
            state = 502
        return state

    def is_model_loaded(self):
        return self.model_loaded

    def load_classes(self):
        with open(CLASSES_DIR, 'r') as file:
            self.class_index = json.load(file)

