""" Work out the first ten digits of the sum of the 50-digit numbers in
numbers.txt. """

import time
import math

with open('numbers.txt') as f:
  numbers = [s.rstrip() for s in f.readlines()]

K = len(numbers)
ndigits = 10

def strsum(s1, s2):
  """ Sum two numbers represented in base 10 in string format. """
  l = max(len(s1), len(s2))
  s1 = s1.rjust(l, '0')
  s2 = s2.rjust(l, '0')
  res = ''
  carry = 0
  for i in xrange(l, 0, -1):
    i1 = int(s1[i-1])
    i2 = int(s2[i-1])
    ir = i1 + i2 + carry
    if ir >= 10:
      ir -= 10
      carry = 1
    else:
      carry = 0
    res += str(ir)

  if carry == 1:
    res += '1'

  return res[::-1]

t0 = time.time()

# maximum number of digits that could be affected by carry
n = int(math.log10(9*K))

# we thus only need to keep track of the first ndigits + n digits of each number
nkeep = ndigits + n
numbers_trunc = [s[:nkeep] for s in numbers]

# do the summation
res = numbers_trunc[0]
for i in xrange(1, len(numbers_trunc)):
  res = strsum(res, numbers_trunc[i])

t1 = time.time()

print res[:ndigits]

print 'Took', t1 - t0, 'seconds.'
