""" A Pythaogrean triplet is a set of three natural numbers, a < b < c, for
which
    a**2 + b**2 = c**2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.
"""

import time

s = 1000

t0 = time.time()

max_a = (s - 3)/3
#algorithm = 'naive'
algorithm = 'math'

if algorithm == 'naive':
  found = False
  for a in xrange(1, max_a + 1):
    for b in xrange(a+1, s - a):
      c = s - a - b
      if c <= b:
        continue
      if a*a + b*b - c*c == 0:
        found = True
        break
    if found:
      break
elif algorithm == 'math':
  found = False
  for a in xrange(1, max_a+1):
    bnum = s*s - 2*s*a
    bdenom = 2*(s-a)
    if bnum % bdenom != 0:
      continue
    b = (s*s - 2*s*a)/(2*(s - a))
    c = s - a - b
    if b <= a or c <= b:
      continue
    found = True
    break
else:
  raise Exception('Unknown algorithm.')

t1 = time.time()

if not found:
  print "Couldn't find the requested triplet."
else:
  print 'The numbers are', (a, b, c), 'the product is abc = ', a*b*c

print 'Took', t1 - t0, 'seconds.'
