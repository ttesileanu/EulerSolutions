""" Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum. """

import time

t0 = time.time()
Nmax = 100
sumsq = Nmax*(Nmax+1)*(2*Nmax+1)/6
s = Nmax*(Nmax+1)/2
t1 = time.time()

print s**2 - sumsq

print 'Took', t1 - t0, 'seconds.'
