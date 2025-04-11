import unittest
import random
from src import algorithms


def generate_data(size, min_val, max_val):
    return sorted([random.randint(min_val, max_val) for _ in range(size)])


class TestPalindromeAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("", True),
            ("a", True),
            ("racecar", True),
            ("RaceCar", True),
            ("hello", False),
            ("12321", True),
            ("123abccba321", True),
            ("notapalindrome", False),
            ("Noon", True),
        ]

    def test_iterative(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s):
                self.assertEqual(algorithms.is_palindrome_iterative(s), expected)

    def test_reverse(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s):
                self.assertEqual(algorithms.is_palindrome_reverse(s), expected)

    def test_recursive(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s):
                self.assertEqual(algorithms.is_palindrome_recursive(s), expected)

    def test_join_reverse(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s):
                self.assertEqual(algorithms.is_palindrome_join_reverse(s), expected)

    def test_stack_queue(self):
        for s, expected in self.test_cases:
            with self.subTest(s=s):
                self.assertEqual(algorithms.is_palindrome_stack_queue(s), expected)


if __name__ == "__main__":
    unittest.main()
