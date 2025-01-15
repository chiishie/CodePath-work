import unittest
# Import functions from cruise_functions.py
from Unit7Standard2 import (
    find_cruise_length,
    find_cabin_index,
    count_checked_in_passengers,
)


class TestCruiseFunctions(unittest.TestCase):
    def test_find_cruise_length(self):
        # Provided examples
        self.assertTrue(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
        self.assertFalse(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
        
        # Additional tests
        self.assertTrue(find_cruise_length([1, 2, 3, 4, 5], 5))
        self.assertFalse(find_cruise_length([2, 4, 6, 8], 7))

    def test_find_cabin_index(self):
        # Provided examples
        self.assertEqual(find_cabin_index([1, 3, 5, 6], 5), 2)
        self.assertEqual(find_cabin_index([1, 3, 5, 6], 2), 1)
        self.assertEqual(find_cabin_index([1, 3, 5, 6], 7), 4)
        
        # Additional tests
        self.assertEqual(find_cabin_index([2, 4, 6, 8], 1), 0)  # Insert before first
        self.assertEqual(find_cabin_index([2, 4, 6, 8], 10), 4) # Insert after last

    def test_count_checked_in_passengers(self):
        # Provided examples
        self.assertEqual(count_checked_in_passengers([0, 0, 0, 1, 1, 1, 1]), 4)
        self.assertEqual(count_checked_in_passengers([0, 0, 0, 0, 0, 1]), 1)
        self.assertEqual(count_checked_in_passengers([0, 0, 0, 0, 0, 0]), 0)
        self.assertEqual(count_checked_in_passengers([1, 1, 1, 1, 1]), 5)
        self.assertEqual(count_checked_in_passengers([0, 0, 0, 0]), 0)
        self.assertEqual(count_checked_in_passengers([0, 0, 1, 1]), 2)
        self.assertEqual(count_checked_in_passengers([0, 1]), 1)
        self.assertEqual(count_checked_in_passengers([1]), 1)

        # Additional test
        self.assertEqual(count_checked_in_passengers([]), 0)  # Edge case: empty list

# Run the tests
if __name__ == '__main__':
    unittest.main()
