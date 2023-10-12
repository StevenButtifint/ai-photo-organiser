import timm
import torch
from PIL import Image
import torchvision.transforms as transforms


class ImageClassifier:
    def __init__(self):
        self.model = None

    def setup_model(self):
        self.model = timm.create_model('efficientnet_b3', pretrained=True)
        self.model.eval()

