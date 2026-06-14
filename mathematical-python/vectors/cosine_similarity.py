import numpy as np

def cos_sim(vector_a: list[float], vector_b: list[float]) -> float:
    a = np.array(vector_a)
    b = np.array(vector_b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


a = [2, 4, 5]
b = [509023, 3898023, 9564654]
print(cos_sim(a, b))