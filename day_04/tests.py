import unittest
from passphrase import *


class TestResolvePassphrase(unittest.TestCase):

    def test_simple_passphrase(self):
        self.assertEqual(count_passphrases(["aa bb cc dd ee"]), 1)
        self.assertEqual(count_passphrases(["aa bb cc dd aa"]), 0)
        self.assertEqual(count_passphrases(["aa bb cc dd aaa"]), 1)

    def test_two_lines_passphrase(self):
        self.assertEqual(count_passphrases(
            ["aa bb cc dd ee", "aa bb cc dd ee"]), 2)
        self.assertEqual(count_passphrases(
            ["aa bb cc dd aa", "aa bb cc dd ee"]), 1)
        self.assertEqual(count_passphrases(
            ["aa bb cc dd aa", "bb aa ee cc bb"]), 0)


class TestResolvePassphrasePartTwo(unittest.TestCase):

    def test_simple_not_valid_passphrase(self):
        self.assertEqual(count_passphrases_v2(["oiii ioii iioi iiio"]), 0)
        self.assertEqual(count_passphrases_v2(["abcde xyz ecdab"]), 0)
        self.assertEqual(count_passphrases_v2(["abcde fghij"]), 1)
        self.assertEqual(count_passphrases_v2(["a ab abc abd abf abj"]), 1)
        self.assertEqual(count_passphrases_v2(["iiii oiii ooii oooi oooo"]), 1)

    def test_two_lines_passphrase(self):
        self.assertEqual(count_passphrases_v2(
            ["abcde xyz ecdab", "aa bb cc dd ee"]), 1)
        self.assertEqual(count_passphrases_v2(
            ["iiii oiii ooii oooi oooo", "aeiou uoiea jiiiii"]), 1)
        self.assertEqual(count_passphrases_v2(
            ["aaaaa", "eaeaeaaaa"]), 2)

filename = "input.txt"
puzzle = []
with open(filename) as f:
    data = f.readlines()
for line in data:
    puzzle.append(line.rstrip())

print("----- PUZZLE PASSPHRASES -----\n" + str(count_passphrases(puzzle)))
print("----- PUZZLE PASSPHRASES - Part Two -----\n" +
      str(count_passphrases_v2(puzzle)))

if __name__ == '__main__':
    unittest.main()
