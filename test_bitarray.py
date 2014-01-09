from bitarray import BitArray
import unittest
import sys


class TestBitArray(unittest.TestCase):

    def test_one_bit(self):
        ba = BitArray(32)
        self.assertFalse(ba.get_bit(0))
        self.assertFalse(ba.get_bit(1))
        self.assertFalse(ba.get_bit(4))
        self.assertFalse(ba.get_bit(5))
        self.assertFalse(ba.get_bit(6))

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


if __name__ == '__main__':
    unittest.main()
