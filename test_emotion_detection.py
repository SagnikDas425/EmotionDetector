from unittest import TestCase, main
from EmotionDetection.emotion_detection import emotion_detector

class EmotionDetectorTestCase(TestCase):

    def test_emotion_detector_expect_joy(self):
        text_to_analyse = "I am glad this happened"
        emotions_data = emotion_detector(text_to_analyse)
        self.assertEqual("joy", emotions_data['dominant emotion'])

    def test_emotion_detector_expect_anger(self):
        text_to_analyse = "I am really mad about this"
        emotions_data = emotion_detector(text_to_analyse)
        self.assertEqual("anger", emotions_data['dominant emotion'])

    def test_emotion_detector_expect_disgust(self):
        text_to_analyse = "I feel disgusted just hearing about this"
        emotions_data = emotion_detector(text_to_analyse)
        self.assertEqual("disgust", emotions_data['dominant emotion'])

    def test_emotion_detector_expect_sadness(self):
        text_to_analyse = "I am so sad about this"
        emotions_data = emotion_detector(text_to_analyse)
        self.assertEqual("sadness", emotions_data['dominant emotion'])

    def test_emotion_detector_expect_fear(self):
        text_to_analyse = "I am really afraid that this will happen"
        emotions_data = emotion_detector(text_to_analyse)
        self.assertEqual("fear", emotions_data['dominant emotion'])

main()
