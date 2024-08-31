from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # test joy
        test_1 =emotion_detector('I am glad this happened')
        self.assertEqual(test_1['label'], 'joy')

        # test anger
        test_2 =emotion_detector('I am really mad about this')
        self.assertEqual(test_2['label'], 'anger')

        # test disgust
        test_3 =emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test_3['label'], 'disgust')

        # test sadness
        test_4 =emotion_detector('I am so sad about this')
        self.assertEqual(test_4['label'], 'sadness')

        # test fear
        test_5 =emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test_5['label'], 'fear')

    unittest.main()
        