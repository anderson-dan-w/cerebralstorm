sum_mult_below :: (Integral a) => a -> a -> a -> a
sum_mult_below top m1 m2 = sum $ filter (\x -> x `mod` m1 == 0 || x `mod` m2 == 0) [1,2..top-1]

sum_mult_below 1000 3 5
