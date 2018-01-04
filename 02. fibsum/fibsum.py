""" By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms. """

import time

t0 = time.time()

s = 0

# g(n) := f(3n-1) = f(3n-2) + f(3n-3) = 2*f(3n-3) + f(3n-4)
#       = 3*f(3n-4) + 2*f(3n-5) = 3*g(n) + 2*f(3n-5)
#       = 3*g(n-1) + 2*h(n-1)
# h(n) := f(3n-2) = f(3n-3) + f(3n-4) = 2*f(3n-4) + f(3n-5)
#       = 2*g(n-1) + h(n-1)

gn = 2
hn = 1

# g1 = 2, h1 = 1 ==> g2 = 8, h2 = 5 ==> g3 = 34, h3 = 21 ==> ...

MAX = 4000000

while gn <= MAX:
  s += gn

  gn, hn = (3*gn + 2*hn, 2*gn + hn)

t1 = time.time()

# check
h1 = 1
h2 = 2
s_again = 0
while h2 <= MAX:
  if h2 % 2 == 0:
    s_again += h2
  h1, h2 = (h2, h1 + h2)

if s != s_again:
  print 'Did this wrong, "fast" version yields', s, 'slow yields', s_again

print s
print 'time', t1 - t0, 'seconds'
