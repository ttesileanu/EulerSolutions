""" How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

Hint: 1 Jan 1900 was a Monday.
"""

import time

t0 = time.time()

# This is probably overkill, but for fun: we will calculate number of days since
# year 1 CE to a given date. This can then easily be used to calculate the
# required value.

# length of months, assuming non-leap year
month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def absolute_days(day, month, year):
  """ Number of days since year 1 to day/month/year. """
  # first get the number of days from 1.1.1 to 1.1.year
  # we will need the number of years that passed...
  nyears = year - 1
  # ...the number of multiples of 4...
  nx4 = nyears / 4
  # ...the number of multiples of 100...
  nx100 = nyears / 100
  # ...and the number of multiples of 400
  nx400 = nyears / 400
  # the number of leap years is then easy to calculate
  nleap = nx4 - nx100 + nx400

  # so number of days from 1.1.1 to 1.1.year is...
  days_to_jan1 = nyears*365 + nleap

  # now find number of days from 1.1.year to 1.month.year
  days_to_month1 = sum(month_length[:(month-1)])

  # if we're past february, we need to know whether this is a leap year
  if month > 2 and year%4 == 0 and (year%400 == 0 or year%100 != 0):
    days_to_month1 += 1

  # now we can calculate the full number of days
  return days_to_jan1 + days_to_month1 + (day - 1)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday']

def get_weekday(day, month, year):
  """ Find on what weekday day/month/year fell. """
  # Jan 1, 1900 was 693 595 days after Jan 1, 1, and it was a Monday; that's a
  # multiple of 7! Therefore, Jan 1, 1 also was a Monday.
  return days[absolute_days(day, month, year)%7]

n_sundays = 0
for year in xrange(1901, 2000+1):
  for month in xrange(1, 12+1):
    if get_weekday(1, month, year) == 'Sunday':
      n_sundays += 1

t1 = time.time()

# tests
#print 'Jan 1, 1:', absolute_days(1, 1, 1)
#print 'Sep 11, 2001:', absolute_days(11, 9, 2001)
#print 'July 4, 1776:', absolute_days(4, 7, 1776)
#print 'Dec 11, 435:', absolute_days(11, 12, 435)
#print 'Nov 17, 1983:', absolute_days(17, 11, 1983)
#print 'Dec 10, 1984:', absolute_days(10, 12, 1984)
#print 'Dec 11, 35:', absolute_days(11, 12, 35)
#print 'Dec 11, 3:', absolute_days(11, 12, 3)
#print 'Dec 11, 135:', absolute_days(11, 12, 135)
#print 'Jan 1, 135:', absolute_days(1, 1, 135)
#print 'Jan 1, 1900:', absolute_days(1, 1, 1900)  # 693 595

print "Number of Sundays from Jan 1, 1901 to Dec 31, 2000 is {}.".format(
      n_sundays)

print "Took {:.0f} us".format(1000000*(t1 - t0))
