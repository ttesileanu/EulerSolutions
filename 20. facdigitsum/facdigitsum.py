""" Calculate the sum of the digits of 100!. """

import time

N = 100

t0 = time.time()

factorial = reduce(lambda x, y: x*y, xrange(1, N+1), 1)
digit_sum = sum([int(s) for s in str(factorial)])

t1 = time.time()

print "The sum of the digits of {}! is {}.".format(N, digit_sum)

print "Took {:.2f} ms.".format(1000*(t1 - t0))
