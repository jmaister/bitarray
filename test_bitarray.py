from bitarray import BitArray
import unittest
import sys


class TestBitArray(unittest.TestCase):

    def test_one_bit(self):
        ba = BitArray(32)
        for i in xrange(32):
            self.assertFalse(ba.get_bit(i))

        ba.set_bit(5)
        self.assertTrue(ba.get_bit(5))
        self.assertFalse(ba.get_bit(4))
        self.assertFalse(ba.get_bit(6))

    def test_small_array(self):
        ba = BitArray(10)
        self.assertFalse(ba.get_bit(6))

        ba.set_bit(6)
        self.assertTrue(ba.get_bit(6))

    def test_big_number(self):
        ba = BitArray(2 ** 32)
        bignum = 2 ** 20
        self.assertFalse(ba.get_bit(bignum))

        ba.set_bit(bignum)
        self.assertTrue(ba.get_bit(bignum))
        self.assertFalse(ba.get_bit(bignum + 1))
        self.assertFalse(ba.get_bit(bignum - 1))

    def test_memory_size(self):
        small = BitArray(10)
        smallsize = sys.getsizeof(small.bitarray)
        self.assertEqual(72, smallsize, 'Small BitArray size')

        big = BitArray(2 ** 32)
        bigsize = sys.getsizeof(big.bitarray)
        self.assertEqual((2 ** (32 - 3)) + 72, bigsize, 'Big BitArray size')

    def test_initialize(self):
        ba = BitArray(10, 1)
        for i in xrange(10):
            self.assertTrue(ba.get_bit(i))

    def test_reset(self):
        ba = BitArray(10, 1)
        for i in xrange(10):
            self.assertTrue(ba.get_bit(i))

        ba.reset_bit(6)
        self.assertFalse(ba.get_bit(6))

    """
    def test_max_memory(self):
        # 4gb of numbers
        bignum = 32 * 1024 * 1024 * 1024
        ba = BitArray(bignum)

        self.assertFalse(ba.get_bit(bignum))

        ba.set_bit(bignum)
        self.assertTrue(ba.get_bit(bignum))
    """

if __name__ == '__main__':
    unittest.main()
