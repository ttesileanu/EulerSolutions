{-
A numer is called 0-to-9 pandigital if contains all the digits from 0 to 9 in
some order. The number 1406357289 is 0-to-9 pandigital, but it also has a
rather interesting sub-string divisibility property.

Let d_i be the ith digit of the number. Note that
  - d_2 d_3 d_4 = 406 is divisible by 2
  - d_3 d_4 d_5 = 063 is divisible by 3
  - d_4 d_5 d_6 = 635 is divisible by 5
  - d_5 d_6 d_7 = 357 is divisible by 7
  - d_6 d_7 d_8 = 572 is divisible by 11
  - d_7 d_8 d_9 = 728 is divisible by 13
  - d_8 d_9 d_10 = 289 is divisible by 17

Find the sum of all 0-to-9 pandigital numbers with this property.
-}

-- Q: would a number starting with a zero count as 0-to-9 pandigital?

{-
Let's try the following strategy: find all possible d_8 d_9 d_10's by looking
at the multiples of 17 between 11 and 987 (numbers <= 10 or >987 have repeated
digits). There are 58 such numbers. Ensure that they don't have repeated
digits, and if they don't, go to the next step:

Find all d_5 d_6 d_7's by looking at the multiples of 7 between
11 and 987. There are 140 such numbers. This time, we can also impose the
condition that d_6 must be a 0 or a 5, which automatically enforces the
condition that 5 | d_4 d_5 d_6. We also make sure that d_5 d_6 d_7 do not
overlap with any of d_8 d_9 d_10.

Finally, find all d_2 d_3 d_4's by looking at all the even numbers between
11 and 987. There are 488 such numbers. We need to make sure that d_2 d_3 d_4
do not overlap with any of the digits chosen before.

In total, we have a maximum of 58*140*488 = 3962560 numbers to test, which is
just over 9% more than all the permutations of the 10 digits. Comparing to
generating all the permutations, this approach should be more efficient, because
we have more ways of dropping out early from the loops.
-}

-- get a list of digits for a k-digit number
getDigits 1 n = [n]
getDigits k n = (n `rem` 10):(getDigits (k - 1) (n `quot` 10))

-- check for repeated elements
hasReps [] = False
hasReps (x:xs) = (elem x xs) || (hasReps xs)
-- acting directly on 3-digit integers
hasRepsInt = hasReps . (getDigits 3)

-- checking whether a pair of lists have repetitions
-- this doesn't check for repetitions within each list
jointReps [] l = False
jointReps (x:xs) l = (elem x l) || (jointReps xs l)
-- acting directly on 3-digit integers
jointRepsInt x y = jointReps (getDigits 3 x) (getDigits 3 y)

-- find out the digit that doesn't appear
remDig n1 n2 n3 = notThere [0..9] ((getDigits 3 n1) ++ (getDigits 3 n2) ++ (getDigits 3 n3))
  where
    notThere l1 l2 = head $ filter (not . (`elem` l2)) l1

main = do
  -- get all multiples of 17, 7, and 2
  let mul17 = [17,34..987]
  let mul7 = [14,21..987]
  let mul2 = [12,14..987]
  -- find the ones that don't have repeated digits
  let mul17Good = filter (not . hasRepsInt) mul17
  let mul2Good = filter (not . hasRepsInt) mul2
  -- d_6 should be a multiple of 5
  let mul7Good = filter (\ n -> (not (hasRepsInt n)) && ((n `quot` 10) `rem` 10) `rem` 5 == 0) mul7

  -- for each valid d_8 d_9 d_10, find all valid d_5 d_6 d_7's
  let pairs1 = [(x, y) | x <- mul17Good, y <- mul7Good, not (jointRepsInt x y)]
  -- for each valid d_5 .. d_10, find all valid d_2 d_3 d_4
  let pairsTotal = [(xy, z) | xy <- pairs1, z <- mul2Good, (not (jointRepsInt (fst xy) z)) && (not (jointRepsInt (snd xy) z))]

  -- now form the whole numbers
  let toTest = [(fst $ fst xyz) + (snd $ fst xyz)*1000 + (snd xyz)*1000000 + (remDig (fst $ fst xyz) (snd $ fst xyz) (snd xyz))*1000000000 | xyz <- pairsTotal]

  -- now check that all the other divisibility constraints are obeyed
  let check345 n = ((n `quot` 100000) `rem` 1000) `rem` 3 == 0
  let check678 n = ((n `quot` 100) `rem` 1000) `rem` 11 == 0
  let check789 n = ((n `quot` 10) `rem` 1000) `rem` 13 == 0
  let goodOnes = filter (\ n -> (check345 n) && (check678 n) && (check789 n)) toTest

  putStrLn "The 0-to-9 pandigitals that have the substring divisilibity property are"
  print goodOnes
  putStrLn $ "Their sum is " ++ show (sum goodOnes) ++ "."
