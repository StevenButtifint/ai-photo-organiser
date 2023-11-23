import unittest
import sys

sys.path.append("../backend")

from photo_classifier import PhotoClassifier


class TestPhotoClassifier(unittest.TestCase):
    def test_setup_model(self):
        photo_classifier = PhotoClassifier()
        photo_classifier.setup_model()
        self.assertEqual(True, photo_classifier.is_model_loaded())

    def test_load_classes(self):
        photo_classifier = PhotoClassifier()
        state, _ = photo_classifier.setup_model()
        self.assertEqual(200, state)


if __name__ == "__main__":
    unittest.main()
