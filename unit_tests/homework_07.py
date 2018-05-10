from unittest.mock import patch
import unittest
import sys

import warm_up
import animal_functions
import fortune_improved

class Homework07(unittest.TestCase):

    def setUp(self):
        self.animals = [
            ['jane clawston', 'cat', 10],
            ['franz catka', 'cat', 2],
            ['sam', 'snake', 99],
            ['gertrude', 'goat', 99]
        ]


    def tearDown(self):
        del self.animals

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


    def test_find_by_name_01(self):
        try:
            actual_out = animal_functions.find_by_name("sam", self.animals)
            self.assertEqual(["sam", "snake", 4], actual_out)
        except:
            self.fail("Failure: find_by_name does not find an existing animal")


    def test_find_by_name_02(self):
        try:
            actual_out = animal_functions.find_by_name("derp", self.animals)
            self.assertIsNone(actual_out)
        except:
            self.fail("Failure: find_by_name does not return None when an animal is not found")


    def test_stringify_animals_01(self):
        try:
            actual_out = animal_functions.stringify_animals(self.animals)
            self.assertEqual(
                "1 - jane clawston, cat\n2 - franz catka, cat\n3 - sam, snake\n4 - gertrude, goat",
                actual_out
            )
        except:
            self.fail("Failure: stringify_animals does not correctly arrange the animals")


    def test_get_most_urgent_01(self):
        try:
            actual_out = animal_functions.get_most_urgent(self.animals)
            self.assertEqual(
                ["gertrude", "goat", 99]
                actual_out
            )
        except:
            self.fail("Failure: get_most_urgent does not find the most urgent animal")
            
