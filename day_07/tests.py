import unittest
from recursive_circus import *


class TestRecursiveCircus(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(recursive_circus(
            [
                {"name": "foo", "childs": ["foo1", "foo2", "foo3"]},
                {"name": "bar1"},
                {"name": "foo1"},
                {"name": "foo2"},
                {"name": "foo3"},
                {"name": "bar", "childs": ["bar1"]},
                {"name": "spam", "childs": ["foo", "bar"]}
            ]), "spam")


# class TestMemoryReallocationPartTwo(unittest.TestCase):

#     def test_get_indexes_of_item_in_array(self):
#         self.assertEqual(get_indexes_of_item_in_array(
#             "foo", ["foo", "bar", "spam", "foo"]), (0, 3))

#     def test_4_slots_v2(self):
#         self.assertEqual(recursive_circus_v2([0, 2, 7, 0]), 4)


puzzle = format_input("input.txt")
print("----- RECURSIVE CIRCUS -----\nPart one result: " +
      str(recursive_circus(puzzle)))

# print("Part two result: " +
#       str(recursive_circus_v2([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6])))


if __name__ == '__main__':
    unittest.main()
