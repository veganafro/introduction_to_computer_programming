from unittest.mock import patch
import unittest
import sys

import encode_decode

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
            actual_out = encode_decode(args)
            expected_out = "ACCZAY"
            self.assertEqual(expected_out, actual_out)
        except:
            self.fail("Failure: num_to_let")


    def test_num_to_let_2(self):
        try:
            args = "1-??-3"
            expected_out = "AC"
            actual_out = encoded_decode(args)
            self.assertEqual(expected_out, actual_out)
