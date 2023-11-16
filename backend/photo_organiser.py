import os
import sys
import glob
import json

from photo_classifier import PhotoClassifier
from constants import *


class PhotoOrganiser:
    def __init__(self, directory):
        self.status = 200
        self.directory = directory
        self.finished = False
        self.photo_paths = []
        self.photo_count = 0
        self.classification_list = []
        self.classification_dictionary = {}
        self.photo_classifier = PhotoClassifier()

    def validate_directory(self):
        if not os.path.isdir(self.directory):
            self.status = 400
        elif not os.path.exists(self.directory):
            self.status = 404

    def set_photo_paths(self):
        self.photo_paths = glob.glob(os.path.join(self.directory, '*.jpg'))
        self.photo_count = len(self.photo_paths)

    def load_classifier(self):
        if not self.photo_classifier.is_model_loaded():
            self.status = self.photo_classifier.setup_model()

    def set_classification_list(self):
        self.classification_list = []
        for photo_dir in self.photo_paths:
            try:
                preprocessed_image = self.photo_classifier.preprocess_photo(photo_dir)
                image_classification = self.photo_classifier.classify_photo(preprocessed_image)
                self.classification_list.append([image_classification, photo_dir])
            except FileNotFoundError:
                self.status = 503

    def set_classification_dictionary(self):
        self.classification_dictionary = {}
        for key, value in self.classification_list:
            if key in self.classification_dictionary:
                self.classification_dictionary[key].append(value)
            else:
                self.classification_dictionary[key] = [value]

    def output_status(self, message):
        formatted = [message, self.status, self.finished, status_codes[self.status]]
        print(json.dumps(formatted), flush=True)
        if self.status != 200:


def process_request(folder_path):
    photo_organiser = PhotoOrganiser(folder_path)
            quit()


if __name__ == "__main__":
    folder_directory = str(sys.argv[1])
    process_request(folder_directory)
