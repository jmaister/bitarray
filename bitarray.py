#!/bin/python
import platform


class BitArray():

    def __init__(self, max_number):
        bits = platform.architecture()[0]
        if bits == '64bit':
            self.bits = 64
        else:
            self.bits = 32

        num_buckets = (max_number / self.bits) + 1
        self.bitarray = [0] * int(num_buckets)
        # 4 or 8
        self.bytes = int(self.bits / 8)
        # 0x000F or 0x000000FF
        self.bit_mask = int('1' * self.bytes, 2)
        pass

    def set_bit(self, n):
        # 4 bits --> 0xF for the bit mask
        bucket = n >> self.bytes
        bit = n & self.bit_mask
        self.bitarray[bucket] = self.bitarray[bucket] | (1 << bit)

    def get_bit(self, n):
        # 4 bits --> 0xF for the bit mask
        bucket = n >> self.bytes
        bit = n & self.bit_mask
        return self.__is_set(self.bitarray[bucket], bit)

    def __is_set(self, n, bit):
        return (n & (1 << bit)) != 0
