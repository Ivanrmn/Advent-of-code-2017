import unittest
from infinite_matrix import *

class TestResolveInfiniteMatrix(unittest.TestCase):

	def test_simple_row(self):
		self.assertEqual(getMaximumMatrixSize(9), 3)
		self.assertEqual(getMaximumMatrixSize(11), 5)
		self.assertEqual(getMaximumMatrixSize(14), 5)
		self.assertEqual(getMaximumMatrixSize(22), 5)
		self.assertEqual(getMaximumMatrixSize(1), 1)
		self.assertEqual(getMaximumMatrixSize(26), 7)

	def test_resolve_infinite_matrix(self):
		self.assertEqual(resolveInfiniteMatrix(22), 3)
		self.assertEqual(resolveInfiniteMatrix(8), 1)
		self.assertEqual(resolveInfiniteMatrix(7), 2)
		self.assertEqual(resolveInfiniteMatrix(9), 2)

		self.assertEqual(resolveInfiniteMatrix(19), 2)
		self.assertEqual(resolveInfiniteMatrix(17), 4)
		self.assertEqual(resolveInfiniteMatrix(7), 2)
		self.assertEqual(resolveInfiniteMatrix(6), 1)
		
		self.assertEqual(resolveInfiniteMatrix(16), 3)
		self.assertEqual(resolveInfiniteMatrix(4), 1)
		self.assertEqual(resolveInfiniteMatrix(13), 4)
		self.assertEqual(resolveInfiniteMatrix(18), 3)
		self.assertEqual(resolveInfiniteMatrix(3), 2)

		self.assertEqual(resolveInfiniteMatrix(12), 3)
		self.assertEqual(resolveInfiniteMatrix(11), 2)
		self.assertEqual(resolveInfiniteMatrix(10), 3)
		self.assertEqual(resolveInfiniteMatrix(25), 4)
		self.assertEqual(resolveInfiniteMatrix(2), 1)

print str(resolveInfiniteMatrix(312051))

if __name__ == '__main__':
	unittest.main()