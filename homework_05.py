import unittest
import analyze_numbers

class Homework_05(unittest.TestCase):

    def test_analyze_true(self):
        self.assertTrue(analyze_numbers.is_odd(69))

    def test_analyze_false(self):
        self.assertFalse(analyze_numbers.is_odd(66))
        
if __name__ = '__main__':
    unittest.main()
