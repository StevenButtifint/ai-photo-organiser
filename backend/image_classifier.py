import timm
import torch
from PIL import Image
import torchvision.transforms as transforms


class ImageClassifier:
    def __init__(self):
        self.model = None

