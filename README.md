bitarray
========

Full Python implementation of a bitarray.

Memory optimization: It packs 32 or 64 bits on a float. Depending on the platform.

Blog entry with explanation on: [jordiburgos.com/post/2014/python-bitarray-sieve-Eratosthenes.html](http://jordiburgos.com/post/2014/python-bitarray-sieve-Eratosthenes.html)

Usage:

    MAX = 2^^32

    ba = BitArray(MAX, initialize=1)
    for n in xrange(2, MAX, 2):
        ba.reset_bit(n)
    
    ba.set_bit(120)
    
    if ba.get_bit(120):
        pass

Sample usage on pysieve.py
