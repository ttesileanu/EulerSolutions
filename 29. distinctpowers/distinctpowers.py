""" How many distinct terms are in the sequence generated by a**b for
      2 <= a <= 100, 2 <= b <= 100?
"""

import time

a_min = 2
b_min = 2
a_max = 100
b_max = 100

t0 = time.time()

terms = {a**b for a in xrange(a_min, a_max+1) for b in xrange(b_min, b_max+1)}

t1 = time.time()

print ("There are {} distinct terms in a**b for {} <= a <= {}, {} <= b <= {}.".
  format(len(terms), a_min, a_max, b_min, b_max))

print "Took {:.2f} ms.".format(1000*(t1 - t0))
