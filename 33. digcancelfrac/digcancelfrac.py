""" Start with a fraction in which both the numerator and the denominator
contain two digits. Suppose one of the digits appears both in the numerator and
the denominator, and suppose the fraction has the property that naively
"simplifying" it by removing the repeated digit yields a correct result. We call
this a "curious fraction". The curious fraction is non-trivial provided the
digit that we're removing is not 0.

There are exactly four non-trivial examples of this type that are less than 1.
Write the product of these fractions in non-reducible form and output the value
of the denominator of this product.
"""

import time

t0 = time.time()

# Suppose we write the fraction as ab/cd. We can't have two repeated digits, as
# then either ab == cd and the fraction is equal to 1 (and thus not less than
# 1), or cd == ba, in which case the fraction is ab/ba and is certainly
# different form 1 (what you would get by naively simplifying both digits).

# So we have one repeated digit. Where is it located?
# We can't have ab/ac = b/c:
#   (10*a + b)/(10*a + c) = b/c implies 10*a*c + b*c = 10*a*b + b*c
#   --> b = c -- contradiction (we said we can't have two repeated digits)
#       (and a can't be zero as then the numerator and denominator wouldn't have
#        two digits each)

# We also can't have ab/cb = a/c:
#   (10*a + b)/(10*c + b) = a/c implies 10*a*c + b*c = 10*a*c + a*b
#   --> b*c = a*b --> a = c -- contradiction
#   (can't have two repeated digits, and b can't be zero or we'll have a trivial
#    curious fraction)

# So the fraction must look like ab/bc = a/c. We need b > a to make sure it's
# smaller than 1 -- note that b = a doesn't work:
#   aa/ac = a/c  -->  11*a/(10*a + c) = a/c --> 11*a*c = 10*a*a + a*c
#     --> 10*a*c = 10*a*a --> a = c (since a can't be zero)

# The  condition we're after is
# (10*a + b)/(10*b + c) = a/c --> 10*a*c + b*c = 10*a*b + a*c
#   --> 9*a*c + b*c = 10*a*b
#   --> (10*a - c)*b = 9*a*c
#   --> b = 9*a*c/(10*a - c)

fractions = []
redfracs = []
for a in xrange(1, 10):
  for c in xrange(1, 10):
    u = 9*a*c
    l = 10*a - c
    if u%l == 0:
      b = u/l 
      if b > a and b < 10:
        # don't really need the full fractions
        fractions.append((10*a + b, 10*b + c))
        redfracs.append((a, c))

# don't need the full product
#product = reduce(lambda x, y: (x[0]*y[0], x[1]*y[1]), fractions, (1, 1))
red_product = reduce(lambda x, y: (x[0]*y[0], x[1]*y[1]), redfracs, (1, 1))

# now we need to bring this to the irreducible form
def gcd(a, b):
  """ Find the gcd of two integers. """
  # ensure a <= b
  if a > b:
    a, b = b, a

  while a > 1:
    a, b = b%a, a

  return b

t1 = time.time()

print fractions
#print product
#print red_product

print "The denominator in the irreducible form of the fraction obtained by "
print "multiplying the four non-trivial curious fractions is {}.".format(
  red_product[1]/gcd(*red_product))

print "Took {:.2f} us.".format(1000000*(t1 - t0))
