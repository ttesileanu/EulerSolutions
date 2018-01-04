""" To each name in names.txt, assign a score by summing the numerical
equivalents of all of its letters (i.e, 'a' = 1, 'b' = 2, ...). Multiply this
score by the index of the name in the *sorted* list to obtain a final score.

What is the total of all the name scores in the file?
"""

import time

t0 = time.time()

# load the names and sort them
with open('names.txt', 'r') as f:
  names = sorted(
            [name.strip('"') for name in ''.join(row for row in f).split(',')])

# get letter score for name
def get_letter_score(name):
  """ Calculate score by summing up all the alphabet scores for the letters in
  the name.
  """
  return sum(ord(c) - ord('A') + 1 for c in name.upper())

scores = [(i+1)*get_letter_score(name) for i, name in enumerate(names)]

t1 = time.time()

print "Total sum of name scores is {}.".format(sum(scores))

print "Took {:.2f} ms.".format(1000*(t1 - t0))
