import numpy as np


a = (10e6/3) + 4*19e8

b = 10e6 + 6*10e8

c = np.pi/4 * 75**2 + (np.pi * 75**2 * 100**2)

print(a+b-c)