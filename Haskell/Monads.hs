import System.IO
import Data.List
import Data.Maybe
import Control.Monad

-- ($) :: (a -> b) -> a -> b
-- (<$>) :: Functor f => (a -> b) -> (f a -> f b)
normsort = sort [1..10] ++ [2..5]
--[1,2,3,4,5,6,7,8,9,10,2,3,4,5]
dollardemosort = sort $ [1..10] ++ [2..5]
--[1,2,2,3,3,4,4,5,5,6,7,8,9,10]
{- infixr 0 $
    This means that it is RIGHT associative and has the lowest precedence possible
-}

-- (.) :: (b->c) -> (a-> b) -> a -> c


a = [1..50]

lazyFib :: [Integer]
lazyFib = map fib [1,2..]
    where 
        fib 0 = 0
        fib 1 = 1
        fib n = fib (n-1) + fib (n-2)
