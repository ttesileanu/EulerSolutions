/* A number n is called abundant if the sum of its proper divisors exceeds n.
The smallest abundant number is 12. It can be shown that all integers greater
than 28123 can be written as a sum of two abundant numbers.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
*/

#include <iostream>
#include <vector>

#include <cmath>

int int_pow(int a, int n)
{
  if (n == 0) return 1;
  if (n == 1) return a;

  const int b = int_pow(a, n/2);
  const int b2 = b*b;
  if (n % 2 == 0) {
    return b2;
  } else {
    return b2*a;
  }
}

int main()
{
  // numbers >= threshold guaranteed to be writable as sum of 2 abundants
  const int threshold = 28124;

  // let us start by finding all abundant numbers < threshold
  // first, find the divisor sums for all these numbers
  int divisor_sums[threshold] = {0};

  divisor_sums[2] = 1;

  for (int n = 3; n < threshold; ++n) {
    // find the lowest divisor (which will be prime)
    int divisor = 0;
    if (n % 2 == 0) {
      divisor = 2;
    } else {
      const int p_max = std::sqrt(n);
      for (int p = 3; p <= p_max; p += 2) {
        if (n % p == 0) {
          divisor = p;
          break;
        }
      }
    }

    if (divisor == 0) {
      // n is prime
      divisor_sums[n] = 1;
    } else {
      // find the power of this divisor
      int mu = 1;
      int i = n / divisor;
      while (i % divisor == 0) {
        i /= divisor;
        ++mu;
      }

      /* the proper divisors of n = (p**mu)*m are all the divisors minus n
         all the divisors of n are
          - all the divisors of m
          - all the divisors of m times p
          - all the divisors of m times p**2
          ...
          - all the divisors of m times p**mu
      */
      const int m = n/int_pow(divisor, mu);
      const int m_all_div_sum = divisor_sums[m] + m;
      divisor_sums[n] = -n;
      for (int i = 0; i <= mu; ++i) {
        divisor_sums[n] += m_all_div_sum*int_pow(divisor, i);
      }
    }
  }

  // now find all the numbers n for which divisor_sums[n] > n
  std::vector<int> abundants;
  for (int n = 0; n < threshold; ++n) {
    if (divisor_sums[n] > n)
      abundants.push_back(n);
  }

  // find all sums of abundant numbers that are < threshold
  bool writeable_as_sum[threshold] = {false};

  for (auto i1 = abundants.begin(); i1 != abundants.end(); ++i1) {
    if (*i1 > threshold/2)
      continue;
    for (auto i2 = i1; i2 != abundants.end(); ++i2) {
      const int n = *i1 + *i2;
      if (n < threshold)
        writeable_as_sum[n] = true;
    }
  }

  int non_sums = 0;
  int sum_of_non_sums = 0;
  for (int i = 0; i < threshold; ++i) {
    if (!writeable_as_sum[i]) {
      ++non_sums;
      sum_of_non_sums += i;
    }
  }

  std::cout << "There are " << non_sums << " numbers that cannot be written "
            << "as a sum of two abundant numbers below " << threshold << "."
            << std::endl;
  std::cout << "The sum of these numbers is " << sum_of_non_sums << "."
            << std::endl;

  return 0;
}
