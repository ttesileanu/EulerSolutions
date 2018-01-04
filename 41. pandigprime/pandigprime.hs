{-
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital; it is
also prime.

What is the largest n-digit pandigital prime that exists?
-}

{-
The sum of the digits of an n-digit pandigital is \sum_{k=1}^n k = n(n+1)/2.
Since a number is divisible by 3 iff the sum of its digits is divisible by 3,
n-digit pandigitals can't be prime if 3 | n or 3 | (n+1). Thus, the only values
of n we need to look at are 1, 4, and 7. The only 1-digit pandigital is 1, which
is not prime, so we only have to look at 4-digit and 7-digit pandigitals.
-}

{-
Furthermore, the last digit of a prime number (with more than one digit) can't
be 2, 4, 5, 6, or 8; thus, we know that the last digit for the pandigitals we 
are interested in must be one of {1, 3, 7, 9}.
-}

-- integer part of square root
isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral

-- check whether a number is prime
is_prime :: Int -> Bool
is_prime 1 = False
is_prime n = let totest = 2:[3,5..(isqrt n)]
  in
    foldr (\ p r -> (n `rem` p) /= 0 && r) True totest

-- prepend element to each list in list of lists
prepend_each :: a -> [[a]] -> [[a]]
prepend_each _ [] = []
prepend_each x (l:ls) = (x:l):(prepend_each x ls)

-- generate all permutations of a list
gen_perms :: [Int] -> [[Int]]
gen_perms [] = [[]]
gen_perms xs = concat $ map (\ x -> prepend_each x $ gen_perms (filter (\ n -> n /= x) xs)) xs

-- turn list of lists into list of integers
toint_each ls = let
    toint = foldl (\ n d -> 10*n + d) 0
  in
    map toint ls

main = putStrLn $ "Maximum pandigital prime is " ++ show (maximum $ filter is_prime ((toint_each $ gen_perms [1..4]) ++ (toint_each $ gen_perms [1..7]))) ++ "."
