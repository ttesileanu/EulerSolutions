{-
The first two consecutive numbers to have two distinct prime factors are:
  14 = 2 x 7
  15 = 3 x 5
The first three consecutive numbers to have three distinct prime factors are:
 644 = 2**2 x  7 x 23
 645 = 3    x  5 x 43
 646 = 2    x 17 x 19

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
-}

import Data.List (find)
import Data.Maybe (fromJust)

-- import Debug.Trace

-- all the prime numbers
primes = 2 : [i | i <- [3,5..],
          and [rem i p > 0 | p <- takeWhile ((<=i).(^2)) primes]]

-- divide k by p as much as possible
exhaustiveDivide k p 
  | (mod k p) == 0 = exhaustiveDivide (k `quot` p) p
  | otherwise = k

-- get prime factors; stop if more than pmax
primeFactors :: Integer -> Integer -> [Integer]
primeFactors n 0 = []
primeFactors 1 _ = []
primeFactors n pmax = lowest:(primeFactors (exhaustiveDivide n lowest) (pmax-1))
  where
    lowest = fromJust $ find (\ p -> (rem n p) == 0) primes

-- starting at n0, move upwards, and stop when n numbers have been found that
-- have exactly n distinct prime factors; assumes that count already have been
-- found
stopWhen :: Integer -> Integer -> Integer -> Integer
stopWhen n0 n count
  | count == n = n0 - n
  | toInteger (length (primeFactors n0 (n+1))) == n = stopWhen (n0+1) n (count+1)
  | otherwise = stopWhen (n0+1) n 0

main = putStrLn $ "First 4 consecutive integers with 4 distinct prime factors start at " ++ show (stopWhen 6 4 0) ++ "."
