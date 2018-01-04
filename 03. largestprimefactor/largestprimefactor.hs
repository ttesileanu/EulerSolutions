{- What is the largest prime factor of the number 600851475143? -}

import Data.List (find)
import Data.Maybe (fromMaybe)

number = 600851475143

-- find smallest prime factor
smallest_prime_factor n = fromMaybe 0 (find (\ k -> (n `rem` k) == 0) (2 : [3, 5..(floor (sqrt (fromIntegral n)))]))

-- find prime factors
prime_factors n = let p = smallest_prime_factor n
  in
    if p == 0 then
      [n]
    else
      p : (prime_factors (n `quot` p))

-- find largest prime factor
largest_prime_factor = last . prime_factors

main = putStrLn $ "Largest prime factor of " ++ show number ++ " is " ++ show (largest_prime_factor number)
