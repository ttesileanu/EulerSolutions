""" Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits. Exclude 1.
"""

import time

p = 5

t0 = time.time()

# The largest sum of k digits, each raised to the pth power, is k*9**p; a
# k-digit number is between 10**(k-1) (inclusive) and 10**k (exclusive). Thus,
# if we want the digit to equal the sum of its digits each raised to the pth
# power, we need 10**(k-1) <= k*9**p < 10**k. So we must have
#   10**(k-1)/k <= 9**p
# (10**(k-1)/k is increasing for all integers k >= 1)

# consider (k-1)log(10) - log(k) - (k-1)*log(9) + log(4)
# d/dk = log(10/9) - 1/k = 0.105 - 1/k --> minimum at k = 9.49; it's about 0.031
# --> 10**(k-1)/k > 0.25*9**(k-1) (for k >= 1)

# therefore 9**(k-1) < 4*9**p --> k - 1 < p + 0.631 --> k < p + 1.631 --> 
#   k <= p + 1

sum_dig_pow = lambda n: sum(int(digit)**p for digit in str(n))

matching = [n for n in xrange(2, 10**(p+1)) if sum_dig_pow(n) == n]

t1 = time.time()

print (("The numbers that are equal to the sum of the {}th powers of "+ 
        "their digits are:").format(p))
print matching
print "Their sum is {}.".format(sum(matching))

print "Took {:.2f} seconds.".format(t1 - t0)
