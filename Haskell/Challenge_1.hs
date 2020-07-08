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

dropN :: Eq a => [a] -> Int -> [a]
dropN xs n = dropN' xs n 
    where   dropN' [] _ = []
            dropN' (x:xs) 1  = dropN' xs n 
            dropN' (x:xs) k = x : dropN' xs (k-1)

splt :: Eq a => [a] -> Int -> ([a], [a])
splt xs n = (take n xs, drop n xs)

slice :: [a] -> Int -> Int -> [a]
slice xs i k | i>0 = take (k-i+1) $ drop (i-1) xs 

rotate :: [a] -> Int -> [a]
rotate xs n = take len . drop (n `mod` len) . cycle $ xs
    where len = length xs

range :: Int -> Int -> [Int]
range x y = [x..y]

combinations :: Int -> [a] -> [[a]]
combinations 0 _ = [[]]
combinations n xs = [y:ys | y:xs' <-tails xs , ys <- combinations (n-1) xs]

lazyPrimes :: [Integer]
lazyPrimes = sieve (2:[3,5..])
    where
        sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p > 0]

a = take 20 lazyPrimes

lazyFib :: [Integer]
lazyFib = map fib [1,2..]
    where 
        fib 0 = 0
        fib 1 = 1
        fib n = fib (n-1) + fib (n-2)

b = take 20 lazyFib

lazyLetters :: [Char]
lazyLetters = ['a', 'b'..]

c = take 20 lazyLetters

d = take 20 [1,2..]


