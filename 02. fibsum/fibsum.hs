{- By considering the terms in the Fibonacci sequence whose values do not
exceed 4 000 000, find the sum of the even-valued terms. -}

{- Let's define
    g(n) := f(3n-1) = f(3n-2) + f(3n-3) = 2*f(3n-3) + f(3n-4)
          = 3*f(3n-4) + 2*f(3n-5) = 3*g(n) + 2*f(3n-5)
          = 3*g(n-1) + 2*h(n-1)
    h(n) := f(3n-2) = f(3n-3) + f(3n-4) = 2*f(3n-4) + f(3n-5)
          = 2*g(n-1) + h(n-1)
   where f(n) is the Fibonacci sequence. We have
    g(1) = f(2) = 2,
    h(1) = f(1) = 1
   and it is straightforward to show by induction that g(n) is even while h(n)
   is odd. Moreover, f(3n) = f(3n-1) + f(3n-2) = g(n) + h(n), is also odd. We
   thus see that only the terms f(3n-1) = g(n) are even in the Fibonacci
   sequence, so they are the only ones we need to worry about.
-}

{- Note that this also implies
    g(n) = 3*g(n-1) + 2*(2*g(n-2) + h(n-2)) = 3*g(n-1) + 4*g(n-2) + 2*h(n-2)
         = 3*g(n-1) + 4*g(n-2) + g(n-1) - 3*g(n-2)
         = 4*g(n-1) + g(n-2)
-}

{- g(1) = 2, g(2) = f(5) = 8 -}

max_fib = 4000000

fib_even_seq = 2 : 8 : zipWith (\ a b -> a + 4*b) fib_even_seq (tail fib_even_seq)

-- sum all g(n) such that g(n) <= 4000000
value = sum [x | x <- takeWhile (<= max_fib) fib_even_seq]

main = putStrLn $ "The sum of the even Fibonacci-sequence numbers smaller than or equal to " ++ show max_fib ++ " is " ++ show value
