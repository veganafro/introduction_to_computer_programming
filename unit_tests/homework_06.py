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


    def test_num_to_let(self):
        
