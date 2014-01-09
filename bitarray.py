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

    def set_bit(self, n):
        # 4 bits --> 0xF for the bit mask
        bucket = n >> 4
        bit = n & 0x0000000F
        self.bitarray[bucket] = self.bitarray[bucket] | (0x80000000 >> bit)

    def get_bit(self, n):
        # 4 bits --> 0xF for the bit mask
        bucket = n >> 4
        bit = n & 0x0000000F
        return self.__is_set(self.bitarray[bucket], bit)

    def __is_set(self, n, bit):
        return (n & (0x80000000 >> bit)) != 0
