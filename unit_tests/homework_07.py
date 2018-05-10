from unittest.mock import patch
import unittest
import sys

import warm_up
import animal_functions
import fortune_improved

class Homework07(unittest.TestCase):

    def test_get_unique_values_01(self):
        try:
            args = []
            actual_out = warm_up.get_unique_values(
                args
            )
            self.assertEqual([], actual_out)
        except:
            self.fail("Failure: get_unique_values does not handle empty list")
