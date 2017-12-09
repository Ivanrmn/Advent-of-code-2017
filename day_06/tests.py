import unittest
from memory_reallocation import *


class TestMemoryReallocation(unittest.TestCase):

    def test_4_slots(self):
        self.assertEqual(memory_reallocation([0, 2, 7, 0]), 5)


class TestMemoryReallocationPartTwo(unittest.TestCase):

    def test_get_indexes_of_item_in_array(self):
        self.assertEqual(get_indexes_of_item_in_array(
            "foo", ["foo", "bar", "spam", "foo"]), (0, 3))

    def test_4_slots_v2(self):
        self.assertEqual(memory_reallocation_v2([0, 2, 7, 0]), 4)


print("----- MEMORY REALLOCATION -----\nPart one result: " +
      str(memory_reallocation([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6])))

print("Part two result: " +
      str(memory_reallocation_v2([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6])))


if __name__ == '__main__':
    unittest.main()
