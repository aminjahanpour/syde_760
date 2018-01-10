import numpy as np

A = np.array([[3,1],
              [1,2]])
B = np.array([9,8])
x = np.linalg.solve(A, B)
print(x)