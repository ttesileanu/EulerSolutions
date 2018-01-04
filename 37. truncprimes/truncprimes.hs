{- Find the sum of all the 11 primes that are both truncatable from left to
right and from right to left.

A prime is truncatable from left to right (or right to left) if removing digits
from left to right (or right to left) yields only primes.

For example, 3797 is truncatable from both sides: 3797, 797, 97, and 7 are all
primes, as are 3797, 379, 37, and 3.

Note: Do not count 2, 3, 5, and 7 as truncatable primes.
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

-- generate right-to-left truncatable primes obtained by starting with a seed
-- and adding one digit to the right
gen_rl_trunc :: Int -> [Int]
gen_rl_trunc n = filter is_prime $ map (\ d -> 10*n + d) [1, 3..9]

-- generate all right-to-left truncatable primes, up to n digits
-- n should be >= 2
gen_all_rl :: Int -> [Int]
gen_all_rl n = fst $ gen_all_rl0 n
  where
    gen_all_rl0 :: Int -> ([Int], [Int])
    gen_all_rl0 1 = ([], []) -- excluding 2, 3..7
    gen_all_rl0 2 = let res = concatMap gen_rl_trunc [2, 3, 5, 7]
      in
        (res, res)
    gen_all_rl0 n = let (all_to_n1, just_n1) = gen_all_rl0 (n-1)
                        newer = concatMap gen_rl_trunc just_n1
      in
        (all_to_n1 ++ newer, newer)

-- integer part of logarithm base 10
ilog10 :: Int -> Int
ilog10 = floor . (logBase 10) . fromIntegral

-- test whether a number of left-to-right truncatable prime
is_lr_trunc :: Int -> Bool
is_lr_trunc 0 = True
is_lr_trunc n = (is_prime n) && (is_lr_trunc $ n `rem` 10^(ilog10 n))

main = do
  putStrLn "The sum of all double truncatable primes is"
  print $ sum $ filter is_lr_trunc $ gen_all_rl 8 
