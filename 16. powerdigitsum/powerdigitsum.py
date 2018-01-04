""" What is the sum of the digits of the number 2**1000?
"""

import time

N = 1000

t0 = time.time()

digit_sum = sum(int(s) for s in list(str(2**N)))

t1 = time.time()

print "Digit sum for 2**{} is {}".format(N, digit_sum)

print "Took {:.0f} us".format(1000000*(t1 - t0))
