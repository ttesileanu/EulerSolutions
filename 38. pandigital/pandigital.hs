{- Consider the 9-digit numbers obtained by concatenating the products of an
integer with (1, 2, ..., n) for n > 1. What is the largest such number so that
the concatenated products form a permutation of the 9 nonzero digits?

For example, take 192 and multiply by 1, 2, and 3:
  192 x 1 = 192 ;  192 x 2 = 384 ;  192 x 3 = 576
which concatenated read 192384576, a 1-to-9 pandigital.

Another example: 9 multiplied by (1,2,3,4,5) yields 918273645, another 1-to-9
pandigital.
-}

--import Data.Array
import Data.List (sort, find)
import Data.Maybe (fromJust)

-- turn number into list
num_to_list 0 = []
num_to_list i = (num_to_list $ i `quot` 10) ++ [i `rem` 10]

-- turn list into number
list_to_num [] = 0
list_to_num l = 10*list_to_num (init l) + (last l)

-- generate concatenated products of x with (1, 2, ..., n), as lists, until the
-- result reaches or exceeds 9 digits; if it exceeds 9 digits, return empty
-- list, otherwise return the concatenated product (as a list)
conc_prod x = conc_prod0 [] x 1
  where
    conc_prod0 l x k
      | (length l) == 9 = l
      | (length l) > 9 = []
      | otherwise = conc_prod0 (l ++ num_to_list (x*k)) x (k+1)

-- check that a list contains all of the digits
check_all_dig l = (sort l) == [1..9]

-- check that a number satisfies the properties of the question
check_pan_prod = check_all_dig . conc_prod
    
main = do
  putStrLn "The largest number whose concatenated products give a pandigital is"
  print $ largest
  putStrLn "This product is"
  print $ list_to_num $ conc_prod largest
  where
    largest = fromJust $ find check_pan_prod [9876, 9875..0]
