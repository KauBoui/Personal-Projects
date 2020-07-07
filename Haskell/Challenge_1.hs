import Data.List
import System.IO
import System.Random

myLast :: [a] -> a
myLast [] = error "Empty Set N/A"
myLast x = x !! (length x-1)

myButLast :: [a] -> a
myButLast [] = error "Empty Set N/A"
myButLast x = x !! (length x-2)

elemAt :: [a] -> Int -> a
elemAt [] x = error "Empty Set N/A"
elemAt l x = l !! (x - 1)

isPalindrome :: Eq a => [a] -> Bool
isPalindrome [] = True
isPalindrome [_] = True
isPalindrome l = l == reverse l 

quicksort :: Ord a => [a] -> [a]
quicksort [] = [] 
quicksort (p:xs) = quicksort lesser ++ [p] ++ quicksort greater
    where
        lesser = filter (<p) xs
        greater = filter (>=p) xs

compress :: Eq a => [a] -> [a]
compress = map head . group

pack :: Eq a => [a] -> [[a]]
pack [] = []
pack (x:xs) = let (first, rest) = span (==x) xs
                in (x:first) : pack rest

encode :: Eq a => [a] -> [(Int, a)]
encode xs = map (\x -> (length x, head x)) (group xs)

dupli :: Eq a => [a] -> [a]
dupli [] = []
dupli (x:xs) = x:x:dupli xs

repli :: Eq a => [a] -> Int -> [a]
repli [] i = []
repli xs i = concatMap (replicate i) xs

lazyPrimes :: [Integer]
lazyPrimes = sieve (2:[3,5..])
    where
        sieve (p:xs) = p : sieve [x|x <- xs, x `mod` p > 0]


