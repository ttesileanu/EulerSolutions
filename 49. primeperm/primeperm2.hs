{- The arithmetic sequence 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime; and (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
-}

-- a much nicer (though slower) solution, taken from wiki.haskell.org

import Data.List

-- all the prime numbers
primes = 2 : [i | i <- [3,5..],
          and [rem i p > 0 | p <- takeWhile ((<=i).(^2)) primes]]

-- check whether a number is prime
isPrime n = elem n $ takeWhile (<=n) primes

primes4 = filter isPrime [1000..9999]
 
soln = [ [a,b,c] | a <- primes4,
                   b <- dropWhile (<= a) primes4,
                   sort (show a) == sort (show b),
                   let c = 2 * b - a,
                   c `elem` primes4,
                   sort (show a) == sort (show c) ]

-- concatenate the integers in a list into one big string
catList [] = ""
catList (x:xs) = (show x) ++ (catList xs)

-- main = print soln

main = do
  let others = filter (not . (1487 `elem`)) soln in
    print $ (read (catList $ head others) :: Integer)
