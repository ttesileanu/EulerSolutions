-- Find the sum of all numbers under one million which are palindromic in base
-- 10 and in base 2.
-- Leading zeros should not be included when deciding the palindrome property.
-- Example: 585 = 1001001001 (binary) is palindromic in both bases.

import Data.List (foldl')

-- convert number to binary
-- NB: binrep 0 --> [] instead of 0!
binrep :: Integral a => a -> [a]
binrep 0 = []
binrep x = binrep (x `quot` 2) ++ [x `rem` 2]

-- test whether the number is a binary palindrome
isbinpal :: Integral a => a -> Bool
isbinpal x = let fwd = binrep x
  in
    fwd == (reverse fwd)

-- generate a short palindrome from a list, e.g.: 32 -> 232
shortpal :: [a] -> [a]
shortpal [] = []
shortpal (x:xs) = reverse xs ++ [x] ++ xs

-- generate a long palindrome from a list, e.g.: 32 -> 2332
longpal :: [a] -> [a]
longpal l = reverse l ++ l

-- generate all the n-element lists made up with elements of l
generate :: Int -> [a] -> [[a]]
generate 0 l = [[]]
generate n l = (extend l) $ generate (n-1) l
  where
    extend :: [a] -> [[a]] -> [[a]]
    extend [] q = []
    extend (x:xs) q = (map (x:) q) ++ (extend xs q)

-- generate all the palindromes made up with up to n letters from l
-- this does not generate palindromes starting with (anything equal to) 0
-- XXX this code only works when n is even
genpal :: Integral a => Int -> [a] -> [[a]]
genpal 0 l = [[]]
genpal n l = let shorter = genpal (n-2) l
                 k = n `quot` 2
                 half = filter (\ x -> (last x) /= 0) $ generate k l
  in
    shorter ++ (map shortpal $ half) ++ (map longpal $ half)

-- turn lists of integers into integers
list_to_int :: [Int] -> Int
list_to_int = foldl' (\ z x -> 10*z + x) 0

-- generate palindromic numbers with up to n digits
-- XXX this code only works when n is even
genpalnum :: Integral a => Int -> [Int]
genpalnum n = map list_to_int $ genpal n [0..9]

main = do
  putStrLn "The sum of the double palindromes less than 1000000 is"
  print $ sum $ filter isbinpal $ genpalnum 6
