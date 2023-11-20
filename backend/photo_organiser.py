import os
import sys
import glob
import json
import nltk
import shutil
from nltk.corpus import wordnet
from scipy.cluster.hierarchy import linkage, fcluster

from photo_classifier import PhotoClassifier
from constants import *


class PhotoOrganiser:
    def __init__(self, directory):
        self.status = 200
        self.directory = None
        self.finished = False
        self.photo_paths = []
        self.photo_count = 0
        self.clusters = None
        self.cluster_count = 0
        self.cluster_names = None
        self.classification_list = []
        self.classification_dictionary = {}
        self.classification_cluster_dictionary = {}
        self.set_directory(directory)
        self.photo_classifier = PhotoClassifier()

    def set_directory(self, directory):
        if os.path.isdir(directory):
            self.directory = directory
        else:
            self.status = 400

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

    def set_linkage_matrix(self):
        distance_matrix = []
        class_labels = self.get_dictionary_classification_list()
        for label1 in class_labels:
            row = []
            synset1 = wordnet.synsets(label1)
            for label2 in class_labels:
                synset2 = wordnet.synsets(label2)
                if synset1 and synset2:
                    similarity = synset1[0].wup_similarity(synset2[0])
                    row.append(similarity if similarity is not None else 0)
                else:
                    row.append(0)
            distance_matrix.append(row)
        linkage_matrix = linkage(distance_matrix, method='average')
        self.linkage_matrix = linkage_matrix

    def create_cluster_dictionary(self):
        class_labels = self.get_dictionary_classification_list()
        linkage_matrix = self.get_linkage_matrix()
        self.clusters = None
        cut_height = linkage_matrix[-1, 2]
        cluster_size_max = len(class_labels) / 4
        max_cluster_size = len(class_labels)
        while max_cluster_size > cluster_size_max:
            self.clusters = fcluster(linkage_matrix, t=cut_height, criterion='distance')
            cluster_sizes = {}
            for cluster in set(self.clusters):
                cluster_sizes[cluster] = self.clusters.tolist().count(cluster)
            max_cluster_size = max(cluster_sizes.values())
            cut_height -= 0.5
        self.set_cluster_count(len(cluster_sizes))
        self.classification_cluster_dictionary = dict(zip(class_labels, self.clusters))

    def create_cluster_names(self):
        self.cluster_names = {}
        for classification, cluster_id in self.classification_cluster_dictionary.items():
            if cluster_id in self.cluster_names:
                self.cluster_names[cluster_id] += "-" + str(classification)
            else:
                self.cluster_names[cluster_id] = str(classification)

    def move_photos(self):
        for classification, cluster_id in self.classification_cluster_dictionary.items():
            photo_directories = self.classification_dictionary[classification]
            folder_name = self.cluster_names[cluster_id]
            if self.create_subfolder(folder_name):
                for directory in photo_directories:
                    if not self.move_file(directory, self.directory + "\\" + folder_name):
                        break
                self.finished = True
            else:
                break

    def output_status(self, message):
        formatted = [message, self.status, self.finished, status_codes[self.status]]
        print(json.dumps(formatted), flush=True)
        if self.status != 200:

    def get_status_code(self):
        return self.status

    def get_photo_count(self):
        return self.photo_count

    def get_cluster_count(self):
        return self.cluster_count

    def get_cluster_names(self):
        return self.cluster_names

    def get_linkage_matrix(self):
        return self.linkage_matrix

    def get_dictionary_classification_list(self):
        return list(self.classification_dictionary.keys())

    def get_classification_dictionary(self):
        return self.classification_dictionary

def process_request(folder_path):
    photo_organiser = PhotoOrganiser(folder_path)
            quit()
def load_wordnet():
    nltk.download(WORDNET)


if __name__ == "__main__":
    load_wordnet()
    folder_directory = str(sys.argv[1])
    process_request(folder_directory)
