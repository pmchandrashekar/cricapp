import unittest
# Assuming your function is in a file named logic.py
# from logic import quicksort 
from mylib import quicksort

class TestQuickSort(unittest.TestCase):

    def test_basic_sort(self):
        """Test a standard unsorted list."""
        self.assertEqual(quicksort.quicksort([5, 2, 4, 3]), [2, 3, 4, 5])

    def test_empty_list(self):
        """Test the base case: an empty list."""
        self.assertEqual(quicksort.quicksort([]), [])

    def test_single_element(self):
        """Test the base case: a single element."""
        self.assertEqual(quicksort.quicksort([1]), [1])

    def test_already_sorted(self):
        """Test a list that is already sorted."""
        self.assertEqual(quicksort.quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        """Test a list sorted in reverse order."""
        self.assertEqual(quicksort.quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        """Test a list with duplicate numbers (crucial for your >= pivot logic)."""
        self.assertEqual(quicksort.quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_negative_numbers(self):
        """Test sorting with negative values."""
        self.assertEqual(quicksort.quicksort([0, -1, 5, -10, 2]), [-10, -1, 0, 2, 5])

if __name__ == '__main__':
    unittest.main()