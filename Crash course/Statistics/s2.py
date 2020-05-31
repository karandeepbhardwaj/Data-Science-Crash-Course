from random import shuffle
from scratch.linear_algebra import sum_of_squares
from s1 import quantile
import math

num_friends = list(range(101))
shuffle(num_friends)

def mean(xs: List[float]) -> float:
    return sum(xs)/len(xs)

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

def de_mean(xs: List[float]) -> float:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    assert len(xs) >= 2
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations)/(n-1)

def standard_deviation(xs: List[float]) -> float:
    return(math.sqrt(variance(xs)))

def interquartile_range(xs: List[float]) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)
