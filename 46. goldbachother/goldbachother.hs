{-
It was proposed by Christian Goldbach that every odd composite (non-prime)
number can be written as the sum of a prime and twice a square.

 9 =  7 + 2 * 1^2
15 =  7 + 2 * 2^2
21 =  3 + 2 * 3^2
25 =  7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
-}

-- all the prime numbers
primes = 2 : [i | i <- [3,5..],
          and [rem i p > 0 | p <- takeWhile ((<=i).(^2)) primes]]

-- check whether a number is prime
isPrime n = elem n $ takeWhile (<=n) primes

-- check whether the conjecture applies to one number, using brute force
-- this also returns True for all primes, so we don't need to avoid them
checkOne n = or $ map isPrime [n - 2 * i*i | i <- takeWhile (\ j -> j*j * 2 + 2 <= n) [0..]]

main = putStrLn $ "The smallest odd composite that disproves the Goldbach conjecture is " ++ show (head (filter (not . checkOne) [3,5..])) ++ "."
