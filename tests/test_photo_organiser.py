import unittest
import sys
import os

sys.path.append("../backend")

from photo_organiser import PhotoOrganiser


class TestPhotoOrganiser(unittest.TestCase):
    def test_set_directory_valid_directory(self):
        valid_current_directory = os.getcwd()
        photo_organiser = PhotoOrganiser(valid_current_directory)
        self.assertEqual(photo_organiser.get_status_code(), 200)

    def test_set_directory_invalid_directory(self):
        photo_organiser = PhotoOrganiser("invalid/directory")
        self.assertEqual(photo_organiser.get_status_code(), 400)

    def test_set_directory_nonexistent_directory(self):
        current_directory = os.getcwd()
        nonexistent_directory = current_directory + "\\not\\existing\\dir"
        photo_organiser = PhotoOrganiser(nonexistent_directory)
        self.assertEqual(photo_organiser.get_status_code(), 400)

    def test_classification_dictionary(self):
        valid_current_directory = os.getcwd()
        photo_organiser = PhotoOrganiser(valid_current_directory)
        photo_organiser.classification_list = [['test_a', 'a'], ['test_b', 'b']]
        photo_organiser.set_classification_dictionary()
        result = photo_organiser.get_classification_dictionary()
        self.assertEqual(result, {'test_a': ['a'], 'test_b': ['b']})

    def test_cluster_names(self):
        valid_current_directory = os.getcwd()
        photo_organiser = PhotoOrganiser(valid_current_directory)
        photo_organiser.classification_cluster_dictionary = {'test_a': 'a', 'test_b': 'b'}
        photo_organiser.create_cluster_names()
        result = photo_organiser.get_cluster_names()
        self.assertEqual(result, {'a': 'test_a', 'b': 'test_b'})


if __name__ == "__main__":
    unittest.main()
