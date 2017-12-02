import unittest
from checksum import resolveChecksum, formatTsvToIntArray, resolveChecksum_partTwo

class TestResolveChecksum(unittest.TestCase):

	def test_simple_row(self):
		self.assertEqual(resolveChecksum([[5, 1, 9, 5]]), 8)
		self.assertEqual(resolveChecksum([[2, 4, 6, 8]]), 6)
		self.assertEqual(resolveChecksum([[5, 4, 9, 5]]), 5)
		self.assertEqual(resolveChecksum([[2, 0, 5]]), 5)
		self.assertEqual(resolveChecksum([[5, 4, 5]]), 1)

	def test_checksums(self):
		self.assertEqual(resolveChecksum([[5, 1, 9, 5],[5, 1, 9, 5],[5, 1, 9, 5]]), 24)
		self.assertEqual(resolveChecksum([[2, 4, 6, 8],[2, 4, 6, 8]]), 12)
		self.assertEqual(resolveChecksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]), 18)

class TestResolveChecksum_partTwo(unittest.TestCase):

	def test_simple_row(self):
		self.assertEqual(resolveChecksum_partTwo([[5, 9, 2, 8]]), 4)
		self.assertEqual(resolveChecksum_partTwo([[9, 4, 7, 3]]), 3)
		self.assertEqual(resolveChecksum_partTwo([[3, 8, 6, 5]]), 2)
		self.assertEqual(resolveChecksum_partTwo([[3, 3, 4, 7]]), 1)

	def test_checksums(self):
		self.assertEqual(resolveChecksum_partTwo([[5, 9, 2, 8],[9, 4, 7, 3],[3, 8, 6, 5]]), 9)
		self.assertEqual(resolveChecksum_partTwo([[3, 3, 4, 7],[2, 1, 5, 3]]), 4)

puzzle = formatTsvToIntArray("input.tsv")
print ("----- RESULT PART ONE -----")
print (resolveChecksum(puzzle))
print ("----- RESULT PART TWO -----")
print (resolveChecksum_partTwo(puzzle))

if __name__ == '__main__':
	unittest.main()