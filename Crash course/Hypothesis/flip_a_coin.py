from typing import Tuple
import math
from scratch.probability import normal_cdf

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    mu = p*n
    sigma = math.sqrt(p*(1-p)*n)
    return mu, sigma

normal_probability_below = normal_cdf

def normal_probability_above(lo: float,
                             mu: float = 0,
                             sigma: float = 1) -> float:
    return 1 - normal_cdf(lo, mu, sigma)

def normal_probability_between(lo: float,
                               hi: flaot,
                             mu: float = 0,
                             sigma: float = 1) -> float:
    return 1 - normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo: float,
                             hi: float,
                             mu: float = 0,
                             sigma: float = 1) -> float:
    return 1 - normal_probability_between(lo, hi, mu, sigma)