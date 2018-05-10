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
            self.assertEqual(["derp", "flerp"], actual_out)
        except:
            self.fail("Failure: get_unique_values does not handle list with unique value in the middle")

    
    def test_get_unique_values_05(self):
        try:
            args = ["flerp", "derp", "derp"]
            actual_out = warm_up.get_unique_values(
                args
            )
            self.assertEqual(["flerp", "derp"], actual_out)
        except:
            self.fail("Failure: get_unique_values does not handle list with unique value at the beginning")

            
    
    def test_get_unique_values_06(self):
        try:
            args = ["derp", "derp", "flerp"]
            actual_out = warm_up.get_unique_values(
                args
            )
            self.assertEqual(["derp", "flerp"], actual_out)
        except:
            self.fail("Failure: get_unique_values does not handle list with unique value at the end")


    def test_create_sentence_01(self):
        try:
            args = ["abderp", "flerp", "axerp", "ahplerp"]
            actual_out = warm_up.create_sentence(
                args
            )
            self.assertEqual("abdaxeahp", actual_out)
        except:
            self.fail("Failure: create_sentence does not create a sentence in the standard case")


    def test_create_sentence_02(self):
        try:
            args = ["herp", "derp", "merp"]
            actual_out = warm_up.create_sentence(
                args
            )
            self.assertEqual("", actual_out)
        except:
            self.fail("Failure: create_sentence does not return an empty string")
