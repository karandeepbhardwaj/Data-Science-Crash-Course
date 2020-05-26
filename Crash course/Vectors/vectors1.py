from typing import List

Vector = List[float]

height_weight_age = [70, 170, 40]
grades = [95, 80, 75, 62]

def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([4,5,6], [1,2,3]) == [3,3,3]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "Emplty List"
    
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Different Sizes"
    
    return [sum(vector[i] for vector in vectors) 
            for i in range(num_elements)]

assert vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16, 20]