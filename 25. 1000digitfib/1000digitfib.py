""" What is the first term in the Fibonacci sequence to contain 1000 digits? """

import time
import math

n_digits = 1000

t0 = time.time()

# taking advantage of Python's ability to work with arbitrarily large integers

# i is F2's index in the Fibonacci sequence
i = 2
F1 = 1
F2 = 1

while True:
  if math.log10(F2)+1 >= n_digits:
    break

  F1, F2 = F2, F1+F2
  i += 1

t1 = time.time()

print (("The {}th term in the Fibonacci sequence is the 1st with more than " +
        "{} digits.").format(i, n_digits))

print "Took {} ms.".format(1000*(t1 - t0))
