import unittest
import numpy as np
import pandas as pd
from src import data_generator
import string

class TestRandomStringFunctions(unittest.TestCase):
    """Test suite for random string generation functions."""
    
    # Test data constants
    STANDARD_SIZES = [5, 10, 15]
    PALINDROME_SIZES = [4, 5, 6, 7]  
    SAMPLE_SIZES = [1, 5, 20]
    LARGE_TEST_SIZE = 100  

    def test_generate_random_string_size(self):
        """Verify generated strings have exactly the requested length."""
        for size in self.STANDARD_SIZES:
            with self.subTest(size=size):
                result = data_generator.generate_random_string(size, False)
                self.assertEqual(len(result), size)

    def test_generate_palindrome(self):
        """Test that palindrome strings are properly generated."""
        for size in self.PALINDROME_SIZES:
            with self.subTest(size=size):
                result = data_generator.generate_random_string(size, True)
                self.assertTrue(result == result[::-1], 
                              f"String '{result}' is not a valid palindrome")

    def test_generate_random_string_content(self):
        """Ensure generated strings only contain lowercase ASCII letters."""
        result = data_generator.generate_random_string(self.LARGE_TEST_SIZE, False)
        self.assertTrue(all(c in string.ascii_lowercase for c in result),
                      "String contains invalid characters")

    def test_get_random_strings_type(self):
        """Verify the function returns a pandas Series."""
        result = data_generator.get_random_strings(5, 10)
        self.assertIsInstance(result, pd.Series)

    def test_get_random_strings_length(self):
        """Test correct number of samples is generated."""
        for samples in self.SAMPLE_SIZES:
            with self.subTest(samples=samples):
                result = data_generator.get_random_strings(5, samples)
                self.assertEqual(len(result), samples)

    def test_get_random_strings_palindromes(self):
        """Verify all strings in the Series are valid palindromes."""
        result = data_generator.get_random_strings(5, 10)
        self.assertTrue(all(s == s[::-1] for s in result),
                      "Found non-palindrome strings")

    def test_edge_cases(self):
        """Test behavior with edge case inputs."""
        # Test invalid size
        with self.assertRaises(ValueError):
            data_generator.generate_random_string(0, True)
        
        # Test minimal valid size
        result = data_generator.generate_random_string(1, True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, result[::-1])

if __name__ == '__main__':
    unittest.main()