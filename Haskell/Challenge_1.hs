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

coprime :: Int -> Int -> Bool
coprime a b = gcd a b == 1

factor :: Int -> [Int]
factor 1 = []
factor n = let prime = head $ dropWhile ((/=0) . mod n) [2..n] in (prime :) $ factor $ div n prime

factorMult :: Int -> [(Int, Int)]
factorMult = map encode . group  . factor
    where encode xs = (head xs, length xs)

totient1 :: Int -> Int
totient1 1 = 1 
totient1 n = length $ filter (coprime n) [1..n-1]

totient2 :: Int -> Int
totient2 n = product [(p-1) * p ^ (c-1) | (p,c) <- factorMult n]

_Y :: (t -> t) -> t
_Y g = g (_Y g)
lazyPrimes :: [Int]
lazyPrimes = [2,3,5,7] ++ _Y ((11:) . tail . gapsW 11 wheel . joinT . hitsW 11 wheel)
joinT ((x:xs):t) = x : union xs (joinT (pairs t))
    where pairs (xs:ys:t) = union xs ys : pairs t
gapsW k (d:w) s@(c:cs)  | k < c     = k : gapsW (k+d) w s
                        | otherwise = gapsW (k+d) w cs
hitsW k (d:w) s@(p:ps)  | k < p     = hitsW (k+d) w s
                        | otherwise = scanl (\c d->c+p*d) (p*p) (d:w) : hitsW (k+d) w ps
wheel = 2:4:2:4:6:2:6:4:2:4:6:6:2:6:4:2:6:4:6:8:4:2:4:2:4:8:6:4:6:2:4:6:2:6:6:4:2:4:6:2:6:4:2:4:2:10:2:10:wheel

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

 
