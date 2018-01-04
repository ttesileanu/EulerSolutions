{- The arithmetic sequence 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime; and (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
-}

import Data.List (nub)

-- all the prime numbers
primes = 2 : [i | i <- [3,5..],
          and [rem i p > 0 | p <- takeWhile ((<=i).(^2)) primes]]

-- check whether a number is prime
isPrime n = elem n $ takeWhile (<=n) primes

-- get pairs of (element, list with element removed)
selections [] = []
selections (x:xs) = (x,xs) : [ (y,x:ys) | (y,ys) <- selections xs ]

-- get permutations of list
permutations :: [a] -> [[a]]
permutations [x] = [[x]]
permutations xs = [ y : zs | (y, ys) <- selections xs , zs <- permutations ys ]

-- generate all groups of n numbers <= k that are monotonically increasing
genInc n k = map reverse (genIncR n)
  where
    genIncR 1 = [ [x] | x <- [0..k] ]
    genIncR n = let shorter = genIncR (n-1)
      in
        [ x:xs | xs <- shorter, x <- [(head xs)..k] ]

-- generate all groups of n numbers <= k that are monotonically increasing and
-- do not start with 0
genIncNoZero n k = filter (\ xs -> (head xs) /= 0) (genInc n k)

-- list to number
listToNum xs = foldl (\ z x -> 10*z + x) 0 xs

-- for a given number (presented as a list), find all prime permutations
findPrimePerms xs = nub $ filter isPrime $ map listToNum $ permutations xs

-- check whether a list is an arithmetic sequence with non-zero step
isArith [] = True
isArith [x] = True
isArith [x, y] = True
isArith (x:(y:xs)) = ((y /= x) && ((y - x) == ((head xs) - y)) && (isArith (y:xs)))

-- generate all n-tuples from a set
genTuples _ 0 = [[]]
genTuples [] _ = []
genTuples (x:xs) n = genTuples xs n ++ map (x:) (genTuples xs $ n - 1)

-- for a given number (presented as a list), find the triplets of prime
-- permutations that are in an arithmetic progression
findTheOnes xs = filter isArith $ genTuples (findPrimePerms xs) 3

-- concatenate the integers in a list into one big string
catList [] = ""
catList (x:xs) = (show x) ++ (catList xs)

main = do
  let res = filter (not . null) $ map findTheOnes $ genIncNoZero 4 9 in
    let others = filter (\ triplets -> (all (not . (1487 `elem`)) triplets)) res in
      print $ (read (catList $ head $ head others) :: Integer)
