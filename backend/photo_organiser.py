import os
import sys
import glob
import json

from image_classifier import ImageClassifier
from constants import *


class PhotoOrganiser:
    def __init__(self):
        self.status = 200
        self.directory = None
        self.finished = False
        self.photo_paths = []
        self.photo_count = 0
        self.classification_list = []
        self.classification_dictionary = {}

    def set_directory(self, directory_path):
        if os.path.isdir(directory_path):
            if os.path.exists(directory_path):
                self.directory = directory_path
            else:
                self.status = 404
        else:
            self.status = 400

    def set_photo_paths(self):
        self.photo_paths = glob.glob(os.path.join(self.directory, '*.jpg'))
        self.photo_count = len(self.photo_paths)

    def load_classifier(self):
        if not self.photo_classifier.is_model_loaded():
            self.status = self.photo_classifier.setup_model()

    def output_status(self, message):
        formatted = [message, self.status, self.finished, status_codes[self.status]]
        print(json.dumps(formatted), flush=True)
        if self.status != 200:
            quit()

