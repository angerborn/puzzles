import unittest
from day05 import is_string_nice, is_super_nice

class TestIsNiceString(unittest.TestCase):
    def test_part1(self):
        self.assertTrue(is_string_nice("ugknbfddgicrmopn"))
        self.assertTrue(is_string_nice("aaa"))
        self.assertFalse(is_string_nice("jchzalrnumimnmhp"))
        self.assertFalse(is_string_nice("haegwjzuvuyypxyu"))
        self.assertFalse(is_string_nice("dvszwmarrgswjxmb"))

    def test_part2(self):
        self.assertTrue(is_super_nice("qjhvhtzxzqqjkmpb"))
        self.assertTrue(is_super_nice("xxyxx"))
        self.assertFalse(is_super_nice("uurcxstgmygtbstg"))
        self.assertFalse(is_super_nice("ieodomkazucvgmuy"))

if __name__ == "__main__":
    unittest.main()
