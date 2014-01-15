#!/bin/python
import platform


class BitArray():

    def __init__(self, max_number, initialize=0):
        bitsstr = platform.architecture()[0]
        if bitsstr == '64bit':
            self.bits = 64
            self.bit_mask = 0x0000003F
            self.bit_offset = 6
        elif bitsstr == '32bit':
            self.bits = 32
            self.bit_mask = 0x001F
            self.bit_offset = 5
        else:
            raise AssertionError('The system is not 32 or 64 bits.')
        num_buckets = (max_number / self.bits) + 1

        if initialize != 0 and initialize != 1:
            raise AssertionError('initialize parameter must be 0 or 1.')

        # 0x0000... or 0xFFFF...
        self.bitarray = [initialize * int('1' * self.bits, 2)] * int(num_buckets)

    def set_bit(self, n):
        bucket, bit = self.__get_address(n)
        self.bitarray[bucket] = self.bitarray[bucket] | (1 << bit)

    def reset_bit(self, n):
        bucket, bit = self.__get_address(n)
        self.bitarray[bucket] = self.bitarray[bucket] & ~(1 << bit)

    def get_bit(self, n):
        bucket, bit = self.__get_address(n)
        return self.__is_set(self.bitarray[bucket], bit)

    def __get_address(self, n):
        # position on the array
        bucket = n >> self.bit_offset
        # bit position on the element
        bit = n & self.bit_mask
        return bucket, bit

    def __is_set(self, n, bit):
        return (n & (1 << bit)) != 0

    def __str__(self):
        st = ''
        n = 0
        for x in self.bitarray:
            st += str(n) + ': ' + bin(x) + '\n'
            n = n + 1
        return st
