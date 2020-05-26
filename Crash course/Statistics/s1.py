from typing import List, Counter


#Find the median 

def _median_odd(xs: List[float]) -> float:
    return sorted(xs)[len(xs)//2]

def _median_even(xs: List[float]) -> float:
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs)//2
    
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
    return _median_even(v) if len(v)%2 == 0 else _median_odd(v)


#Find the quantile
def quantile(xs: List[float], p: float) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

# Find the mode

def mod(x: List[float]) -> float:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]
    
print(set(mod([1,2,3,4,5,5,5,5,6,7,8,9,9,9,3,3,2,2,2])))