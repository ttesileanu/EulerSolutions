-- A number is called a circular prime if all rotations of its digits form
-- prime numbers. An example is 197, since 197, 971, and 719 are all prime. All
-- the circular primes below 100 are 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73,
-- 79, 97.
--
-- How many circular primes are there below one million?
import Data.List (foldl')

-- generate all the n-element lists made up with elements of l
generate :: Int -> [a] -> [[a]]
generate 0 l = [[]]
generate n l = (extend l) $ generate (n-1) l
  where
    extend :: [a] -> [[a]] -> [[a]]
    extend [] q = []
    extend (x:xs) q = (map (x:) q) ++ (extend xs q)

-- generate all the lists with up to n elements of l (excluding 0)
generate_upto :: Int -> [a] -> [[a]]
generate_upto 0 l = []
generate_upto n l = (generate n l) ++ (generate_upto (n-1) l)

-- turn lists of integers into integers
list_to_int :: [Int] -> Int
list_to_int = foldl' (\ z x -> 10*z + x) 0

-- rotate a list by one
rotate :: [a] -> [a]
rotate (x:xs) = xs ++ [x]

-- integer part of square root
isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral

-- check whether a number is prime
is_prime :: Int -> Bool
is_prime 1 = False
is_prime n = let totest = 2:[3,5..(isqrt n)]
  in
    foldr (\ p r -> (n `rem` p) /= 0 && r) True totest

-- generate all rotations of a list
rotate_all :: [a] -> [[a]]
rotate_all l = rotate_all0 l (length l)
  where
    rotate_all0 l 0 = []
    rotate_all0 l n = l:rotate_all0 (rotate l) (n-1)

-- check whether all rotations of a list lead to prime numbers
all_rot_prime :: [Int] -> Bool
all_rot_prime = and . map (is_prime . list_to_int) . rotate_all

-- a counting function
count :: Eq a => a -> [a] -> Int
count x = length . filter (==x)

-- main
main = do
  -- the circular primes with more than one digit can only be made up of digits
  -- 1, 3, 7, or 9
  --   even digits are clearly not good because one of the rotations is bound
  --   to place the even digit in last position
  --   same for 5
  -- so: generate all numbers with up to six digits chosen from 1, 3, 7, 9
  --     for each of them check that all the rotations are prime
  --     if they are, increase the count for circular primes
  -- we need to add 2 for 2 and 5, which are circular but we miss otherwise
  putStr "There are "
  putStr . show $ 2 + (count True $ map all_rot_prime $ generate_upto 6
    [1, 3, 7, 9])
  putStrLn " circular primes below 1000000."
