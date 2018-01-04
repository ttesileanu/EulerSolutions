{-
Triangle, pentagonal, and hexagonal numbers are defined as:
  triangle:     T_n = n*(n+1)/2     [1, 3, 6, 10, 15, ...]
  pentagonal:   P_n = n*(3*n-1)/2   [1, 5, 12, 22, 35, ...]
  hexagonal:    H_n = n*(2n-1)      [1, 6, 15, 28, 45, ...]

  It can be verified that T_{285} = P_{165} = H_{143} = 40755.

  Find the next triangle number that is also pentagonal and hexagonal.
-}

{-
The simplest algorithm is to sweep through the remaining numbers of a particular
type (e.g., triangle) and check for each one whether it obeys the other
properties as well. If it doesn't, move on.

Since our target must satisfy all three properties, we are free to choose which
of the properties to base our sweep on. It's best to use the one that makes the
largest steps, which is the hexagonal series.
-}

-- get integer part of square root
isqrt = floor . sqrt . fromIntegral

-- check whether number is a square
isSquare n = sq * sq == n
    where sq = isqrt n

isTriangle t = (t >= 1 && isSquare (1 + 8*t))
isPentagonal n = (n >= 1 && sqr*sqr == delta && ((1 + sqr) `rem` 6) == 0)
  where
    delta = 1 + 24*n
    sqr = floor $ sqrt $ (fromIntegral delta)

hexagon n = n*(2*n - 1)

nums = [ hn | n <- [144..], let hn = hexagon n, isTriangle hn, isPentagonal hn]

main = do
  print $ head nums
