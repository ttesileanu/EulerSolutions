{- Find the sum of all the multiples of 3 or 5 below 1000. -}

max_n = 1000

main = putStrLn $ "Sum of all multiples of 3 or 5 below " ++ show max_n ++ " is " ++
--  show (sum (map (\ n -> if (n `rem` 3) == 0 || (n `rem` 5) == 0 then n else 0) [1..999]))
  show (sum [x | x <- [1..(max_n-1)], x `mod` 3 == 0 || x `mod` 5 == 0])
