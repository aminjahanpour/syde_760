import random

import numpy as np
from numpy import linalg as LA

A = np.array([[3,1],
              [1,2]])
B = np.array([9,8])
x = np.linalg.solve(A, B)
# print(x)


# p1= np.array(
#     [[0.9, 0.1],
#      [0.2, 0.8]]
#             )

p1 = np.array(
    [[0.1, 0.6, 0.3],
     [0.2, 0.2, 0.6],
     [0.4, 0.4, 0.2]])

p2 = LA.matrix_power(p1, 2)

p_steady = LA.matrix_power(p1, 2000)

print(p1)
print(p2)
print(p_steady)

s = "B"
for i in range(100):
    print(s)

    p_ = random.random()

    if s == "B":
        if p_ <= p1[0][0]:
            ns = "B"
        elif p1[0][0] < p_ <= p1[0][0] + p1[0][1]:
            ns = "S"
        elif p1[0][0] + p1[0][1] < p_:
            ns = "H"

    elif s == "S":
        if p_ <= p1[1][0]:
            ns = "B"
        elif p1[1][0] < p_ <= p1[1][0] + p1[1][1]:
            ns = "S"
        elif p1[1][0] + p1[1][1] < p_:
            ns = "H"

    elif s == "H":
        if p_ <= p1[2][0]:
            ns = "B"
        elif p1[2][0] < p_ <= p1[2][0] + p1[2][1]:
            ns = "S"
        elif p1[2][0] + p1[2][1] < p_:
            ns = "H"

    s = ns
