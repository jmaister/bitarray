from bitarray import BitArray
import math
import time


def sieve(MAX):
    ba = BitArray(MAX, initialize=1)
    for n in xrange(2, MAX, 2):
        ba.reset_bit(n)

    limit = math.sqrt(MAX)
    limit = math.floor(limit)
    limit = int(limit)

    for n in xrange(3, limit, 2):
        if ba.get_bit(n):
            for i in xrange(n * 2, MAX, n):
                ba.reset_bit(i)

    """
    for n in xrange(1, MAX):
        if ba.get_bit(n):
            print "is prime", n
    """
    #print ba


def time_sieve(n):
    t1 = time.time()
    sieve(n)
    t2 = time.time()
    return (t2 - t1)


def main():
    print time_sieve(2 ** 30)


if __name__ == '__main__':
    main()
