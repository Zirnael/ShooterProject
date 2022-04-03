from math import sqrt
from typing import List, Tuple


def normalize(vector: List[int]) -> Tuple[float, float]:
    vectorLength = length(vector)
    if vectorLength == 0:
        return 0, 0
    return vector[0] / vectorLength, vector[1] / vectorLength


def length(vector: List[int]):
    return sqrt(sum(map(lambda x: x ** 2, vector)))
