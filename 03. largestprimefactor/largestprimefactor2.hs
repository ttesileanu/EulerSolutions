{- What is the largest prime factor of the number 600851475143? -}

number = 600851475143

-- keep only those elements whose prime factors list contains only one element
primes = 2 : filter (null . tail . prime_factors) [3, 5..]

prime_factors n = factor n primes
  where
    factor n (p:ps)
      | p*p > n = [n] -- found no proper prime divisors
      | n `rem` p == 0 = p : factor (n `quot` p) (p:ps)
      | otherwise = factor n ps

main = putStrLn $ "Largest prime factor of " ++ show number ++ " is " ++ show (last $ prime_factors number)
