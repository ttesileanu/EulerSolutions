/* Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits. Exclude 1.
*/

#include <iostream>

int pow(int n, int p)
{
  if (p == 0) return 1;
  if (p == 1) return n;

  const int np2 = pow(n, p/2);
  const int np2sq = np2*np2;
  return np2sq*((p%2 == 0)?1:n);
}

int sum_dig_pow(int n, int p)
{
  int sum = 0;
  while (n != 0) {
    sum += pow(n%10, p);
    n /= 10;
  }

  return sum;
}

int main()
{
  const int p = 5;

/* The largest sum of k digits, each raised to the pth power, is k*9**p; a
   k-digit number is between 10**(k-1) (inclusive) and 10**k (exclusive). Thus,
   if we want the digit to equal the sum of its digits each raised to the pth
   power, we need 10**(k-1) <= k*9**p < 10**k. So we must have
     10**(k-1)/k <= 9**p
   (10**(k-1)/k is increasing for all integers k >= 1)

   consider (k-1)log(10) - log(k) - (k-1)*log(9) + log(4)
   d/dk = log(10/9) - 1/k = 0.105 - 1/k --> minimum at k = 9.49; it's about 0.031
   --> 10**(k-1)/k > 0.25*9**(k-1) (for k >= 1)

   therefore 9**(k-1) < 4*9**p --> k - 1 < p + 0.631 --> k < p + 1.631 --> 
     k <= p + 1
*/

  int sum = 0;
  for (int n = 2; n < pow(10, p+1); ++n) {
    if (n == sum_dig_pow(n, p))
      sum += n;
  }
  std::cout << "The sum of the numbers that are equal to the sum of the "
            << p << "th poers of their digits is " << sum << "." << std::endl;

  return 0;
}
