""" What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20? """

import time
import operator

numbers = range(1, 21)

t0 = time.time()

def gcd(a, b):
  if a == 0:
    return b
  if b == 0:
    return a
  if a > b:
    return gcd(a%b, b)
  else:
    return gcd(a, b%a)

def gcm(a, b):
  return a*b / gcd(a, b)

def gcm_n(numbers):
  n = 1
  for i in numbers:
    n = gcm(n, i)

  return n

N = gcm_n(numbers)

t1 = time.time()

print N
print 'Took', t1 - t0, 'seconds.'
