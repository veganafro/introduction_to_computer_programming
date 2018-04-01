import unittest
import analyze_numbers

class AnalyzeNumbers(unittest.TestCase):

    def test_odd_true(self):
        self.assertTrue(analyze_numbers.is_odd(69))

    def test_odd_false(self):
        self.assertFalse(analyze_numbers.is_odd(66))

    def test_prime_true(self):
        self.assertTrue(analyze_numbers.is_prime(7))

    def test_prime_false(self):
        self.assertFalse(analyze_numbers.is_prime(8))

    def test_abundant_true(self):
        self.assertTrue(analyze_numbers.is_abundant(12))

    def test_abundant_false(self):
        self.assertFalse(analyze_numbers.is_abundant())

        
if __name__ == '__main__':
    unittest.main()
