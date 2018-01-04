{- Let p be the perimeter of a right angle triangle with integral length sides
a, b, c. For example, for p = 120, there are exactly three possibilities
  {20, 48, 52}, {24, 45, 51}, {30, 40, 50}

For which value of p <= 1000 is the number of solutions maximized?
-}

-- In a right triangle, c^2 = a^2 + b^2, so p = a+b+c = a+b + sqrt(a^2+b^2), or
-- sqrt(a^2 + b^2) = p - (a + b) --> a^2 + b^2 = p^2 + a^2 + b^2 - 2p(a+b) + 2ab
-- p^2 = 2p(a + b) - 2ab = 2b(p - a) + 2pa --> p^2 - 2pa = 2b(p - a)
-- (p-a)^2 - a^2 = 2b(p-a) --> b = (p/2)(p-2a)/(p-a)

-- note that p-a-b = p-a-(p/2)(p-2a)/(p-a) = ((p-a)^2 - 0.5*p*(p-2a))/(p-a)
--                 = (p^2 + a^2 - 2pa - 0.5*p^2 + pa)/(p-a)
--                 = (0.5*p^2 - pa + a^2)/(p-a)
--                 = 0.5*((p-a)^2 + a^2)/(p-a)
--                 > 0 provided a < p
-- so the solution we found is valid if a < p

-- we will want to represent b as defined above; this is the result of a
-- division, so we will represent it as a quotient and a remainder
data QuotRem = MakeQuotRem Int Int deriving (Show)
get_quot (MakeQuotRem a _) = a
get_rem (MakeQuotRem _ b) = b

-- find b given a and p
find_b :: Int -> Int -> QuotRem
find_b a p = let num = p*(p-2*a)
                 den = 2*(p-a)
  in
    MakeQuotRem (num `quot` den) (num `rem` den)

-- test whether a given a works
test_a a p = let quot_rem = find_b a p
  in
    ((get_rem quot_rem) == 0) && ((get_quot quot_rem) > a)

-- since b = p*(p-2*a)/(2*(p-a)), it can only be integer if p%2 == 0
-- count how many integer right triangles for a given p
add_bool n True = n+1
add_bool n False = n
count_tri p = foldl (\ n a -> (add_bool n (test_a a p))) 0
  [1..(p-1)]

-- find maximum given criterion
find_max :: Ord b => [a] -> (a -> b) -> (a, b)
find_max [x] f = (x, f x)
find_max (x:xs) f = let (x0, b0) = find_max xs f
                        b = f x
  in
    if b > b0
      then (x, b)
      else (x0, b0)

-- solve the problem!
find_most_solns = find_max [2, 4 .. 1000] count_tri

(high_p, high_n) = find_most_solns

main = do
  putStrLn ("Highest number of right triangles obtained at p = " ++
    show high_p ++ " (" ++ show high_n ++ " solutions)")
