{-
1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the sum
  1^1 + 2^2 + 3^3 + ... + 1000^1000.
-}

-- calculate 10^n
ten_pow 0 = 1
ten_pow n = 10*(ten_pow (n-1))

-- calculate a^b modulo n
mod_power a 0 n = 1
mod_power a 1 n = mod a n
mod_power a p n
  | p `mod` 2 == 0 = let res = mod_power a (p `quot` 2) n
    in
      mod (res*res) n
  | otherwise = mod (res*res*a) n
    where
      res = mod_power a ((p-1) `quot` 2) n

-- calculate a+b modulo n
mod_sum a b n = mod (a+b) n

-- calculate 1^1 + 2^2 + 3^3 + ... + k^k modulo n
mod_self_pow 1 n = 1
mod_self_pow k n = mod ((mod_self_pow (k-1) n) + mod_power k k n) n

main = print $ mod_self_pow 1000 $ ten_pow 10
