import matplotlib.pyplot as plt

import numpy as np

A = np.arange(20).reshape(4, 5)
B = np.arange(10).reshape(5, 2)

print(A)
print(B)
C = B.T @ A
print(C)
