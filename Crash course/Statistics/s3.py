from scratch.linear_algebra import dot
from typing import List
from s2 import standard_deviation

from s2 import de_mean

def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys)
    
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

def correlation(xs: List[float], ys: List[float]) -> float:
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x /stdev_y
    else:
        return 0
    
