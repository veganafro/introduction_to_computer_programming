from unittest.mock import patch
import unittest
import sys

import encode_decode
import barcode_utilities

class Homework06(unittest.TestCase):


    class Console(object):

        def __init__(self):
            self.data = []

        
        def write(self, s):
            self.data.append(s)


        def __str__(self):
            return "".join(self.data)


    def test_num_to_let_1(self):
        try:
            args = "1-3-3-26-1-25"
            expected_out = "ACCZAY"
            actual_out = encode_decode.num_to_let(args)
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail("Failure: num_to_let")


    def test_num_to_let_2(self):
        try:
            args = "-1-a-??-3-69-"
            expected_out = "AC"
            actual_out = encode_decode.num_to_let(args)
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail("Failure: num_to_let")


    def test_num_to_let_1(self):
        try:
            args = "AZ"
            expected_out = "1-26"
            actual_out = encode_decode.let_to_num(args)
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail("Failure: let_to_num")


    def test_num_to_let_2(self):
        try:
            args = "!A69Z$"
            expected_out = "1-26"
            actual_out = encode_decode.let_to_num(args)
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail("Failure: let_to_num")


    def test_generate_bar_widths(self):
        try:
            args = "043000181706"
            expected_out = "11132111132141132113211321111111222112132221131232111114111"
            actual_out = barcode_utilities.generage_bar_widths(args)
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail("Failure: generate_bar_widths")


    def test_valid_barcode(self):
        try:
            
            
if __name__ == "__main__":
    unittest.main()
