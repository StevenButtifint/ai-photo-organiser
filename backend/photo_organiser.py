import os
import sys
import glob

from image_classifier import ImageClassifier
from constants import *


class PhotoOrganiser:
    def __init__(self, directory):
        self.directory = directory
        self.image_classifier = ImageClassifier()
        self.image_classifier.setup_model()


