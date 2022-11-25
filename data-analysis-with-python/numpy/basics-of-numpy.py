import numpy as np

a = np.array([1,2,3], dtype='int16')
print("Array a: ", a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print("Array b: ", b)

# Get dimension
print("Dim.: ", a.ndim)

# Get shape
print("Shape: ", a.shape)

# Get type
print("Type: ", a.dtype)
print("Itemsize: ", a.itemsize)

# Get total size
print("Total size: ", a.nbytes)