/* We call an n-digit number (n < 10) '1 through n pandigital' if it makes use
of all the digits 1, ..., n exactly once. For example 15234 is 1 through 5
pandigital.

Find the sum of all products P = X x Y in which the concatenation of P, X, Y is
a 1 through 9 pandigital.

Note that some products can be obtained in more than one way, so be sure to only
include it once in the sum.
*/

#include <iostream>
#include <set>
#include <algorithm>
#include <numeric>

template <class It>
int number(It iter1, It iter2)
{
  int x = 0;
  while (iter1 < iter2) {
    x = 10*x + (*iter1);
    ++iter1;
  }

  return x;
}

int main()
{
  /* suppose X is k-digit, Y is l-digit, and P is m-digit; then k + l + m = 9
    assuming w.l.o.g. that k <= l
    also, 10^{k-1} <= X < 10^k, 10^{l-1} <= Y < 10^l, and so, since X * Y = P,
    10^{k + l  - 2} <= P < 10^{k + l}
    10^{m-1} <= P < 10^m, so
    k + l - 2 < m < k + l + 1 ; m = 9 - k - l
    k + l - 2 < 9 - k - l < k + l + 1
    2*(k + l) - 2 < 9 < 2*(k + l) + 1
    4 < k + l < 11/2 --> k + l = 5 --> k = 1, l = 4 or k = 2, l = 3
  */

  /* Simple approach: generate all 9! permutations, split them according to
    (k, l) = (1, 4) or (2, 3), find the ones that obey X * Y = P, keep track of
    all the Ps
  */

  std::set<int> products;
  int permutation[9];

  for (int i = 1; i <= 9; ++i)
    permutation[i-1] = i;

  int x, y, p;
  while (true) {
    p = number(permutation+5, permutation+9);
    // try k = 1, l = 4
    x = permutation[0];
    y = number(permutation+1, permutation+5);
    if (x*y == p)
      products.insert(p);

    // try k = 2, l = 3
    x = number(permutation, permutation+2);
    y = number(permutation+2, permutation+5);
    if (x*y == p)
      products.insert(p);

    // go to the next permutation
    if (!std::next_permutation(permutation, permutation + 9))
      break;
  }

  int sum = std::accumulate(products.begin(), products.end(), 0);
  std::cout << "The sum of all the pandigital products is " << sum
            << "." << std::endl;

  return 0;
}
