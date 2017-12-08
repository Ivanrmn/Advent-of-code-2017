import unittest
from twisty_trampoline import *


class TestResolveTwistyTrampoline(unittest.TestCase):

    def test_simple_trampoline(self):
        self.assertEqual(resolve_twisty_trampoline([0, 3, 0, 1, -3]), 5)
        self.assertEqual(resolve_twisty_trampoline([2, 1, 3, 0, -1]), 2)


class TestResolveTwistyTrampolinePartTwo(unittest.TestCase):

    def test_simple_trampoline_v2(self):
        self.assertEqual(resolve_twisty_trampoline_v2([0, 3, 0, 1, -3]), 10)
        self.assertEqual(resolve_twisty_trampoline_v2([2, 1, 3, 0, -1]), 2)


filename = "input.txt"
puzzle = []
puzzle_v2 = []
with open(filename) as f:
    data = f.readlines()
for line in data:
    puzzle.append(int(line.rstrip()))
    puzzle_v2.append(int(line.rstrip()))

print("----- TWISTY TRAMPOLINE -----\n Part One result: " +
      str(resolve_twisty_trampoline(puzzle)))

print("----- TWISTY TRAMPOLINE -----\n Part Two result: " +
      str(resolve_twisty_trampoline_v2(puzzle_v2)))

if __name__ == '__main__':
    unittest.main()
