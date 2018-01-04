/* Consider the Collatz sequence: x_n is positive integer, and

    x_{n+1} = | x_n/2     if x_n is even
              | 3*x_n+1   if x_n is odd

    with the condition that the sequence ends when x_n = 1. Given x_0 < 1000000,
    what is the longest Collatz sequence?
*/

#include <iostream>

#include <algorithm>
#include <unordered_map>
#include <vector>

int main()
{
  int N_max = 1000000;

  // keep track of any sequence lengths that we already calculated
  // NB: it turns we need long long, otherwise we get overflow around 100000
  std::unordered_map<long long, int> chain_lengths({{1, 1}});

  for (int x0 = 1; x0 < N_max; ++x0) {
    // we might have already calculated this
    if (chain_lengths.count(x0) == 0) {
      std::vector<long long> chain({x0});
      long long x = x0;
      int known_length;
      while (true) {
        x = ((x%2 == 0) ? (x/2) : (3*x+1));

        if (chain_lengths.count(x) != 0) {
          // we already know what happens from here
          known_length = chain_lengths[x];
          break;
        }

        chain.push_back(x);
      }

      // store the lengths for all the sequences we have found
      for (int i = 0; i < chain.size(); ++i) {
        chain_lengths[chain[i]] = chain.size() - i + known_length;
      }
    }
  }

  // find the longest sequence with starting x0 < N_max
  int max_len = 1;
  int argmax_len = 1;
  for (auto it = chain_lengths.begin(); it != chain_lengths.end(); ++it) {
    if (it -> first < N_max && it -> second > max_len) {
      argmax_len = it -> first;
      max_len = it -> second;
    }
  }

  std::cout << "Starting with " << argmax_len << " yields the longest Collatz "
            << "sequence (" << max_len << " terms)" << std::endl;

  return 0;
}
