import Data.List
import System.IO

-- This is a single-line comment 

{-
This is a multi-line comment
Int: -2^63 to 2^63 
Integer: Size is as big as memory can hold
Floats and Doubles
Bool: True or False
Char - UTC character
Tuples
-}
maxInt = maxBound :: Int
minInt = minBound :: Int

always5 :: Int
always5 = 5 

sumnums = sum[1..1000]

{-
Prefix operators take the form of 
modulo = mod 5 4 
Note: no commas or parens for arguments. 
The operator is a prefix to the arguments 

Alternate way to notate (Infix operator)
modulo2 = 5 `mod` 4
uses ` to 'push' operator to middle
-}

--Negative numbers need parenthesies
negadd = 5 + (-4)

num9 = 9 :: Int
sqrt9 = sqrt(fromIntegral num9)

-- Built in math functions 
pivalue = pi
power9 = exp 9
log9 = log 9
squared9 = 9 ** 2
truncatedval = truncate 9.999
roundval = round 9.999
ceilingval = ceiling 9.999
floorval = floor 9.999
{-
List of Trig funcs: 
sin, cos, tan, asin, acos, atan, sinh, 
cosh, tanh, asinh, acosh, atanh
-}
sinpiover2 = sin (pi / 2)

--Logic operators && || not()


{-
Use :t to querie about a functions inputs, outputs, 
and expected data types
-}

--Lists
primes = [3,5,7,11]
--Finding length of a list
lenprimes = length primes 
--Reverse a list 
revprimes = reverse primes
--check empty
isempty = null primes
--pulling elements out of a list using !! operator by index
just7 = primes !! 2
--pulling first and last element
firstprime = head primes
lastprime = last primes 
--pulling everything but the last element
primeinit = init primes
--pulling just the first X elements
take2primes = take 2 primes
--removing X elements
drop2primes = drop 2 primes
--checking if an element is a member of a list
is3prime = 3 `elem` primes
is7prime = elem 7 primes
--Max and Min in list
maxprime = maximum primes
minprime = minimum primes
--Note ++ is the list concat operator 
moreprimes = primes ++ [13,17,19,23,29]
--populating lists based on patterns
zerototen = [0..10]
evens = [2,4..20]
everyotherletter = ['A','C'..'Z']
{- infinite lazy lists (lazy language means it wont generate the values until 
needed) -}
infinby10s = [10,20..]
-- making repeating elements
its2sallthewaydownbaby = replicate 100 2 
itsstill2sbaby = take 100 (repeat 2)
--cyclical lists
cyclelist = take 20 (cycle [1,2,4,6,8])
--multiply every value
times2 = [x * 3 | x <- [1..10]]
--Note : as a cons operator 
numbers = 2 : 8 : 24 : 52 : []
--Complicated list constraints in 1 line of code
divisibleBy9and13 = [x | x <- [1..500], x `mod` 13 == 0, x `mod` 9 == 0]
--list sorting
sortedlist = sort [3,7,2,1,9,9,4]
-- adding lists elementwise
sumoflist = zipWith (+) [1,1,2,2,3,4] [4,4,3,3,2,1]
-- filtering elements by value
primesgt5 = filter (>5) primes
evensupto20 = takeWhile (<= 20) [2,4..]
-- folding from the left or right 
multofelems = foldl (*) 1 [2,3,4,5]

multTable = [[x * y | y <- [1..100]] | x <- [1..100]]

randTuple = (1, "Random Tuple")


addMe :: Int -> Int -> Int

--function_name param1 param2 = operations (returned value)
addMe x y = x + y

--no need for type declaration if its straight forward
sumMe x y = x + y

addTuple :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuple (x, y) (x2, y2) = (x + x2, y + y2)

--recursive factorial

factorial :: Int -> Int

factorial 0 = 1
factorial n = n * factorial (n - 1)

isOdd :: Int -> Bool
isOdd n
    | n `mod` 2 == 0 = False
    | otherwise = True

isEven :: Int -> Bool
isEven n = n `mod` 2 == 0





























 