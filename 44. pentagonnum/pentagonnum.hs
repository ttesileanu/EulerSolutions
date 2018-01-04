{-
Pentagonal numbers are numbers P_n that can be written as 
  P_n = n*(3n-1)/2
It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference,
70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P_j and P_k, for which their sum and
difference are both pentagonal, and D = abs(P_k - P_j) is minimized.

What is the value of D?
-}

{-
I don't have much insight here, but let's wlog assume P_k > P_j (and thus
k > j, since P_n is increasing for n >= 1). We have
  D = P_k-P_j = (3*(k*k - j*j) - (k-j))/2 = (k-j)*(3*(k+j) - 1)/2
    = d*(3s - 1)/2
where
  d = k - j,   s = k + j

It's easy to check that
  dD/dk > 0  and  Dd/dj < 0   for all k, j

Thus, it seems like a reasonable heuristic is to go in increasing order of k,
and for each k, start at j = k-1 and go down towards j = 0. This, however,
does not guarantee we will find the minimal D first.

Suppose, however, that we keep track of minimal D found to this point. Then we
can stop our downward sweep in j as soon as we've found D(k, j) >= D_min -- we
know that going any lower will only yield larger values for D. We can also do
the same for the k sweep: once D(k, k-1) itself is >= D_min, we know that no
further D(k, j) will ever be smaller. At this point we can stop.

(This solution was inspired by googling...)
-}

import Data.List (find)
import Data.Maybe (fromJust, isNothing)

-- calculate the nth pentagonal number
pentagon n = n*(3*n-1) `quot` 2

-- check whether a number is pentagonal
isPentagon n = (n >= 1 && sqRoot*sqRoot == delta && ((1 + sqRoot) `rem` 6) == 0)
  where
    delta = 1 + 24*n
    sqRoot = floor $ sqrt $ (fromIntegral delta)

-- given k and j, get Pk, Pj and calculate Pk + Pj, Pk - Pj
sumDiff k j = (pk + pj, pk - pj)
  where
      pk = pentagon k
      pj = pentagon j

-- get tuple with minimum first entry, provided the second entry is nonzero
minFirstDefault (d1, 0) (d2, 0) = (d1, 0)
minFirstDefault (d1, i) (d2, 0) = (d1, i)
minFirstDefault (d1, 0) (d2, j) = (d2, j)
minFirstDefault (d1, i) (d2, j)
  | d1 <= d2 = (d1, i)
  | otherwise = (d2, j)

--
search k j dkMin = do
  let (s, d) = sumDiff k j
  let bounty = (isPentagon s) && (isPentagon d)
  let newDKMin = if not bounty then dkMin else minFirstDefault dkMin (d, k)
  if (snd newDKMin) == 0 then
    if j > 1 then
      search k (j-1) newDKMin
    else
      search (k+1) k newDKMin
  else if (d >= (fst newDKMin)) then
    if j < k-1 then
      search (k+1) k newDKMin
    else
      newDKMin
  else if j > 1 then
    search k (j-1) newDKMin
  else
    search (k+1) k newDKMin

main = do
  let dkMin = search 2 1 (0, 0)
  putStrLn $ "The minimum D is " ++ show (fst dkMin) ++ "."
  let pk = pentagon (snd dkMin)
  putStrLn $ "The pair of numbers is " ++ show (pk, pk - (fst dkMin)) ++ "."
