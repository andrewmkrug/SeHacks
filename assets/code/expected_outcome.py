import unittest

class SeleniumHacks(unittest.TestCase):

    def test_everyone_learns(self):
        room = []  # Array of everyone here
        for Person in room:
            self.assertTrue(Person.learned_something_new)