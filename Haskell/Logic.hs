import System.IO
import Data.List

not' :: Bool -> Bool
not' True = False
not' False = True

and' :: Bool -> Bool -> Bool
and' True True = True
and' _ _ = False

or' :: Bool -> Bool -> Bool
or' True _ = True
or' _ True = True 
or' False False = False

nand' :: Bool -> Bool -> Bool
nand' a b = not' (and' a b)

xor' :: Bool -> Bool -> Bool
xor' True  False = True
xor' False True  = True
xor' _ _ = False

impl' :: Bool -> Bool -> Bool
impl' a b = not' a `or'` b

equ' :: Bool -> Bool -> Bool
equ' True True = True
equ' False False = True 
equ' _ _ = False

table :: (Bool -> Bool -> Bool) -> IO ()
table f = mapM_ putStrLn [show a ++ " " ++ show b ++ " " ++ show (f a b) 
                            | a <- [True, False], b <- [True, False]]

