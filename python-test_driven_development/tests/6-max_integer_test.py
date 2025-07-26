#!/usr/bin/python3
"""Unittest for max_integer(list=[])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Empty list should return None"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """List with one element should return that element"""
        self.assertEqual(max_integer([42]), 42)

    def test_sorted_list(self):
        """Sorted list should return last element"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Unsorted list should return the maximum element"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_negative_numbers(self):
        """List of negative numbers"""
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_float(self):
        """List mixing ints and floats"""
        self.assertEqual(max_integer([1, 3.5, 2.2, 3]), 3.5)

    def test_identical_elements(self):
        """All elements identical"""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_none_input(self):
        """None as input should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_in_list(self):
        """Non-numeric element should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])


if __name__ == '__main__':
    unittest.main()
