import timm
import torch
from PIL import Image
import torchvision.transforms as transforms


class PhotoClassifier:
    def __init__(self):
        self.model = None
    def is_model_loaded(self):
        return self.model_loaded

