import numpy as np

a = np.array([1,2,3,4])
a+2
a-2
a*2
a/2

b = np.array([1,0,1,0])
a+b

a**2

np.sin(a)
np.cos(a)

# Linear algebra
a = np.ones((2,3))
b = np.full((3,2),2)
np.matmul(a,b) # matrix multiplication

# Find the determinant
c = np.identiy(3)
np.linalg.det(c)

# Statistics
stats = np.array([[1,2,3],[4,5,6]])
stats
np.min(stats, axis=0)
np.max(stats, axis=1)
np.sum(stats)

