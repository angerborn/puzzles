from not_very_secure import alphanumeric
import unittest

class Tests(unittest.TestCase):

    def test_correct(self):
        self.assertTrue(alphanumeric("helloworld123"))

    def test_incorrect(self):
        self.assertFalse(alphanumeric("hello world_"))

    def test_empty(self):
        self.assertFalse(alphanumeric(""))

if __name__ == "__main__":
    unittest.main()
