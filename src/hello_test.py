import unittest

class TestBinarySearch(unittest.TestCase):
    def test_find_existing_value(self):
        arr = [1, 2, 3, 4, 5]
        x = 4
        result = binary_search(arr, x)
        self.assertEqual(result, 3)

    def test_find_nonexisting_value(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        result = binary_search(arr, x)
        self.assertEqual(result, -1)

    def test_empty_array(self):
        arr = []
        x = 1
        result = binary_search(arr, x)
        self.assertEqual(result, -1)

    def test_single_item_array(self):
        arr = [1]
        x = 1
        result = binary_search(arr, x)
        self.assertEqual(result, 0)

    def test_duplicates(self):
        arr = [1, 2, 2, 3, 4, 5, 5]
        x = 5
        result = binary_search(arr, x)
        self.assertIn(result, [4, 5])

if __name__ == '__main__':
    unittest.main()
