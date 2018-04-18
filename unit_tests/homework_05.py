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
        self.assertEqual("  xxxx", funcynum.horizontal_line(
            "x", # char
            4, # width
            2 # left_padding
        ))


    def test_vertical_lines(self):
        actual_out = funcynum.vertical_lines(
            "x", # char
            2, # height
            1, # left_padding
            2, # number
            0 # interior_offset
        )
        expected_out = """ xx\n xx"""
        self.assertEqual(expected_out, actual_out)

        
    def test_vertical_line(self):
        actual_out = funcynum.vertical_line(
            "x", # char
            2, # height
            2, # left_padding
        )
        expected_out = """  x\n  x"""
        self.assertEqual(expected_out, actual_out)

        
    def test_print_zero(self):
        expected_out = funcynum.print_zero(
            "*",
            5
        ).strip()
        actual_out = "*****\n*   *\n*   *\n*   *\n*****"
        self.assertEqual(expected_out, actual_out)


    def test_print_one(self):
        actual_out = funcynum.print_one(
            "x", # char
            3 # width
        ).strip()
        expected_out = "  x\n  x\n  x\n  x\n  x"
        self.assertEqual(expected_out, actual_out)


    def test_print_two(self):
        actual_out = funcynum.print_two(
            "*", # char
            5 # width
        ).strip()
        expected_out = "*****\n    *\n*****\n*\n*****"
        self.assertEqual(expected_out, actual_out)

    
    def test_print_three(self):
        actual_out = funcynum.print_three(
            "*", # char
            5 # width
        ).strip()
        expected_out = "*****\n    *\n*****\n    *\n*****"
        self.assertEqual(expected_out, actual_out)


    def test_print_four(self):
        actual_out = funcynum.print_four(
            "*",
            5
        ).strip()
        expected_out = "*   *\n*   *\n*****\n    *\n    *"
        self.assertEqual(expected_out, actual_out)


    def test_print_five(self):
        actual_out = funcynum.print_five(
            "*",
            5
        ).strip()
        expected_out = "*****\n*\n*****\n    *\n*****"
        self.assertEqual(expected_out, actual_out)


    def test_print_six(self):
        actual_out = funcynum.print_six(
            "*",
            5
        ).strip()
        expected_out = "*****\n*\n*****\n*   *\n*****"
        self.assertEqual(expected_out, actual_out)


    def test_print_seven(self):
        actual_out = funcynum.print_seven(
            "*",
            5
        ).strip()
        expected_out = "*****\n    *\n    *\n    *\n    *"
        self.assertEqual(expected_out, actual_out)


    def test_print_eight(self):
        actual_out = funcynum.print_eight(
            "*",
            5
        ).strip()
        expected_out = "*****\n*   *\n*****\n*   *\n*****"
        self.assertEqual(expected_out, actual_out)


    def test_print_nine(self):
        actual_out = funcynum.print_nine(
            "*",
            5
        ).strip()
        expected_out = "*****\n*   *\n*****\n    *\n    *"
        self.assertEqual(expected_out, actual_out)


    def test_print_plus(self):
        actual_out = funcynum.print_plus(
            "*",
            5
        ).strip()
        expected_out = "  *\n  *\n*****\n  *\n  *"
        self.assertEqual(expected_out, actual_out)


    def test_print_minus(self):
        actual_out = funcynum.print_minus(
            "*",
            5
        ).strip()
        expected_out = "\n\n*****"
        self.assertEqual(expected_out, actual_out)
        

if __name__ == '__main__':
    unittest.main()
