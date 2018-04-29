from unittest.mock import patch
import unittest
import sys

import encode_decode
import barcode_utilities
import is_palindrome
import pig_latin

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
            self.fail("Failure: num_to_let does not properly handle standard case.")


    def test_num_to_let_2(self):
        try:
            args = "-1-a--??-3-69-"
            expected_out = "AC"
            actual_out = encode_decode.num_to_let(args)
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail(
                "Failure: num_to_let does not properly handle consecutive dashes or non numerics."
            )


    def test_let_to_num_1(self):
        try:
            args = "AZ"
            expected_out = "1-26"
            actual_out = encode_decode.let_to_num(args)
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail("Failure: let_to_num does not properly handle standard case.")


    def test_let_to_num_2(self):
        try:
            args = "!A69Z$"
            expected_out = "1-26"
            actual_out = encode_decode.let_to_num(args)
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail("Failure: let_to_num does not properly handle non alphabetic case.")


    def test_generate_bar_widths(self):
        try:
            args = "043000181706"
            expected_out = "11132111132141132113211321111111222112132221131232111114111"
            actual_out = barcode_utilities.generate_bar_widths(args)
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail("Failure: generate_bar_widths does not generate correct bar widths.")


    def test_valid_barcode_1(self):
        try:
            args = "036000291450"
            actual_out = barcode_utilities.valid_barcode(args)
            self.assertFalse(actual_out)
        except:
            self.fail("Failure: valid_barcode does not properly invalidate incorrect barcode.")


    def test_valid_barcode_2(self):
        try:
            args = "036000291452"
            actual_out = barcode_utilities.valid_barcode(args)
            self.assertTrue(actual_out)
        except:
            self.fail("Failure: valid_barcode does not properly validate correct barcode.")


    def test_valid_barcode_3(self):
        try:
            args = ""
            actual_out = barcode_utilities.valid_barcode(args)
            self.assertFalse(actual_out)
        except:
            self.fail("Failure: valid_barcode does not properly handle empty string case.")


    def test_reverse_1(self):
        try:
            args = ""
            actual_out = is_palindrome.reverse(args)
            self.assertEqual("", actual_out)
        except:
            self.fail("Failure: reverse does not properly handle empty string case.")


    def test_reverse_2(self):
        try:
            args = "derp"
            actual_out = is_palindrome.reverse(args)
            self.assertEqual("pred", actual_out)
        except:
            self.fail("Failure: reverse does not properly handle standard case.")


    def test_is_palindrome_1(self):
        try:
            args = ""
            self.assertTrue(
                is_palindrome.is_palindrome(args)
            )
        except:
            self.fail("Failure: is_palindrome")

    def test_is_palindrome_2(self):
        try:
            args = "derp"
            self.assertFalse(
                is_palindrome.is_palindrome(args)
            )
        except:
            self.fail("Failure: is_palindrome")


    def test_is_palindrome_3(self):
        try:
            args = "gll a llg"
            self.assertTrue(
                is_palindrome.is_palindrome(args)
            )
        except:
            self.fail("Failure: is_palindrome")


    def test_pig_latin_1(self):
        try:
            args = "cannot convert"
            self.assertEqual(
                args,
                pig_latin.to_pig_latin(args)
            )
        except:
            self.fail("Failure: to_pig_latin")


    def test_pig_latin_2(self):
        try:
            args = "aye"
            self.assertEqual(
                "ayeway",
                pig_latin.to_pig_latin(args)
            )
        except:
            self.fail("Failure: to_pig_latin")


    def test_pig_latin_3(self):
        try:
            args = "shut"
            self.assertEqual(
                "utshay",
                pig_latin.to_pig_latin(args)
            )
        except:
            self.fail("Faiulre: to_pig_latin")


    def test_pig_latin_4(self):
        try:
            args = "chut"
            self.assertEqual(
                "utchay",
                pig_latin.to_pig_latin(args)
            )
        except:
            self.fail("Faiulre: to_pig_latin")


    def test_pig_latin_5(self):
        try:
            args = "thut"
            self.assertEqual(
                "utthay",
                pig_latin.to_pig_latin(args)
            )
        except:
            self.fail("Faiulre: to_pig_latin")


    def test_pig_latin_6(self):
        try:
            args = "qaut"
            self.assertEqual(
                "utqaay",
                pig_latin.to_pig_latin(args)
            )
        except:
            self.fail("Faiulre: to_pig_latin")


    def test_pig_latin_7(self):
        try:
            args = "sut"
            self.assertEqual(
                "utsay",
                pig_latin.to_pig_latin(args)
            )
        except:
            self.fail("Faiulre: to_pig_latin")


    def test_pig_latin_8(self):
        try:
            args = "s23"
            self.assertEqual(
                "s23",
                pig_latin.to_pig_latin(args)
            )
        except:
            self.fail("Faiulre: to_pig_latin")
            

if __name__ == "__main__":
    unittest.main()
