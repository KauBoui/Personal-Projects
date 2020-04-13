import Data.List
import System.IO

primes m =  ps where ps = map head $ takeWhile (not.null) $ scanl (\\) [2..m] [[p, p+p..m] | p <- ps]
            


        


