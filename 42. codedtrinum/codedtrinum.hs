{-
A triangle number T is one that can be written as T = (1/2)*n*(n+1). To each
word, assign a value by summing the numbers corresponding to the alphabetical
position of each of its letters. For example, value(SKY) = 19 + 11 + 25 = 55.
Call a word a 'triangle word' if its value is a triangle number.

How many words from words.txt are triangle words? The words are written in
all-caps, are separated by commas, and are surrounded by quotation marks.
-}

import System.IO
import Data.Char (ord)

-- eliminate quotation marks
noQuotes = filter (\ c -> c /= '\"')

-- split string into list of strings, using delimiter
splitBy delimiter = foldr f [[]] 
  where f c l@(x:xs) | c == delimiter = []:l
                     | otherwise = (c:x):xs

-- get word value
wordValue [] = 0
wordValue (c:cs) = (ord(c) - ord('A') + 1) + (wordValue cs)

-- check whether number is square
isSquare n = sq * sq == n
    where sq = floor $ sqrt $ (fromIntegral n::Double)

-- check whether number is triangular
-- T is triangular, T = (1/2)*n*(n+1), iff sqrt(1 + 8*T) is integer
-- note that if it is integer, it will be odd, since 1 + 8*T is odd
isTriangular t = isSquare (1 + 8*t)

main = do
  contents <- readFile "words.txt"
  let words = splitBy ',' $ noQuotes contents
  let count = foldl (\ n s -> if (isTriangular s) then n+1 else n) 0 (map wordValue words)
  putStrLn $ "Number of triangular words is " ++ show count ++ "."
