""" If all the numbers from 1 to 1000 (inclusively) were written out in words,
how many letters would be used?
"""

import time

N = 1000

t0 = time.time()

small = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
          6: 'six', 7: 'seven', 8: 'eight', 9: 'none', 10: 'ten',
          11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
          15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
          19: 'nineteen'};
tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'};

def towords(n):
  """ Writes number out in words, omitting spaces and hyphens.
  Assumes 0 < n <= 1000.
  """
  if n == 1000:
    return 'onethousand'

  hundreds = n/100
  subhundred = n%100
  if hundreds > 0:
    prefix = small[hundreds] + 'hundred'
    if subhundred != 0:
      prefix += 'and'
  else:
    prefix = ''

  if subhundred < 20:
    return prefix + small[subhundred]
  else:
    return prefix + tens[subhundred/10] + small[subhundred%10]

digits_per_number = [len(towords(n)) for n in xrange(1, 1001)]
digit_sum = sum(digits_per_number)

t1 = time.time()

print "Writing out the numbers from 1 to 1000 uses {} letters.".format(
       digit_sum)

print "Took {:.2f} ms.".format(1000*(t1 - t0))
