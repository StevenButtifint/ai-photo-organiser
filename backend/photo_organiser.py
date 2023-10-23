import os
import sys
import glob

from image_classifier import ImageClassifier
from constants import *


class PhotoOrganiser:
    def __init__(self):
        self.status = 200
        self.directory = None
        self.image_classifier = ImageClassifier()
        self.image_classifier.setup_model()


    def set_directory(self, directory):
        if os.path.isdir(directory_path):
            if os.path.exists(directory_path):
                self.directory = directory
            else:
                self.status = 404
        else:
            self.status = 400

