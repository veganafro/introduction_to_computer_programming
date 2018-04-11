import unittest
import analyze_numbers
import clicky_quad as click_quad
import funcynum


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
        self.assertFalse(analyze_numbers.is_abundant(13))

        
class ClickQuadrant(unittest.TestCase):

    def test_upper_right(self):
        self.assertEqual("red", click_quad.get_quadrant_color(12, 12))

        
    def test_lower_right(self):
        self.assertEqual("green", click_quad.get_quadrant_color(12, -12))

        
    def test_upper_left(self):
        self.assertEqual("blue", click_quad.get_quadrant_color(-12, 12))

        
    def test_lower_left(self):
        self.assertEqual("yellow", click_quad.get_quadrant_color(-12, -12))


class Funcynum(unittest.TestCase):

    def test_horizontal_line(self):
        self.assertEqual("  xx", funcynum.horizontal_line("x", 4, 2))


    def test_vertical_lines(self):
        actual_out = funcynum.vertical_lines(
            "x", # char
            2, # height
            1, # left_padding
            2, # number
            0 # interior_offset
        )
        expected_out = """ xx
 xx"""
        self.assertEqual(expected_out, actual_out)

        
    def test_vertical_line(self):
        actual_out = funcynum.vertical_line(
            "x", # char
            2, # height
            2, # left_padding
        )
        expected_out = """  x
          x"""
        self.assertEqual(expected_out, actual_out)
        

if __name__ == '__main__':
    unittest.main()
