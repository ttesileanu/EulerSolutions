{- Champernowne's constant C10 is the irrational number defined by concatenating
the positive integers:
  0.123456789101112131415161718192021...
Let d_n represent the nth digit of the fractional part of C10; for example,
d_12 = 1.

What is d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000?
-}

{- By using the first 9 numbers (1-9), we generate the first 9 digits of
frac(C10). Using the next 90 (10-99), we generate 180 more digits; the next
900 yield the next 2700 digits.

In general, using the numbers from 1 to 10^k - 1 generates
  9 + 2*90 + 3*900 + ... + 9k*10^{k-1} = 9*(1 + 2*10 + 3*100 + ... + k*10^{k-1})
digits of C10.

  We have \sum_{l=0}^k x^l = (x^{k+1} - 1)/(x - 1), and by differentiating,
          \sum_{l=1}^k l x^(l-1) = ((k+1)*x^k*(x-1) - (x^{k+1}-1))/(x-1)^2
                                 = (k*x^{k+1} - (k+1)*x^k + 1)/(x-1)^2
  so the number of digits generated by 10^k - 1 numbers is
    (k*10^{k+1} - (k+1)*10^k + 1)/9
  or
    ((9*k - 1)*10^k + 1)/9

  Number of generated digits is
    M = ((9*log(n + 1) - 1)*(n + 1) + 1)/9
      = (9*(n + 1)*log(n + 1) - n)/9
      = (n + 1)*log(n + 1) - n/9
  where n = 10^k - 1.

  Unfortunately we can't solve for this, so it's of limited utility... However,
  each number we add will be made up of at least one digit, so if we're
  interested in the Mth digit of C10, using all the numbers up to M is a safe
  bet.
-}

-- turn number into list of digits
num_to_list_rev 0 = []
num_to_list_rev n = (n `rem` 10):(num_to_list_rev $ n `quot` 10)
num_to_list = reverse . num_to_list_rev

-- generate the fractional part of C10 by concatenating numbers up to n
-- foldr is fast because it puts things in a form that is tail recursive
gen_c10 n = foldr (\ m acc -> (num_to_list m) ++ acc) [] [1..n]

c10_long = gen_c10 1000000
value = product [c10_long !! (n-1) | n <- [10^k | k <- [0..6]]]

main = do
  putStrLn $ "The value is " ++ show (value) ++ "."
