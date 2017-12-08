import unittest
from memory_reallocation import *


class TestMemoryReallocation(unittest.TestCase):

    def test_4_slots(self):
        self.assertEqual(memory_reallocation([0, 2, 7, 0]), 5)


print ("----- MEMORY REALLOCATION -----\nPart one result: "+str(memory_reallocation([10, 3, 15, 10,	5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6])))

if __name__ == '__main__':
    unittest.main()
