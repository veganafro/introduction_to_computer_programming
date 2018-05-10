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


        
    def test_get_unique_values_02(self):
        try:
            args = ["derp", "derp", "derp"]
            actual_out = warm_up.get_unique_values(
                args
            )
            self.assertEqual(["derp"], actual_out)
        except:
            self.fail("Failure: get_unique_values does not handle list with one unique value")


    
    def test_get_unique_values_03(self):
        try:
            args = ["derp", "herp"]
            actual_out = warm_up.get_unique_values(
                args
            )
            self.assertEqual(["derp", "derp"], actual_out)
        except:
            self.fail("Failure: get_unique_values does not handle list with all unique values")


    
    def test_get_unique_values_04(self):
        try:
            args = ["derp", "flerp", "derp"]
            actual_out = warm_up.get_unique_values(
                args
            )
            self.assertEqual([], actual_out)
        except:
            self.fail("Failure: get_unique_values does not handle list with unique value in the middle")

    
    def test_get_unique_values_05(self):
        try:
            args = ["flerp", "derp", "derp"]
            actual_out = warm_up.get_unique_values(
                args
            )
            self.assertEqual([], actual_out)
        except:
            self.fail("Failure: get_unique_values does not handle list with unique value at the beginning")
