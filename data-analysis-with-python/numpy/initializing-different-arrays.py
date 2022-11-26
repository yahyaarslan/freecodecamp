# All zeros
a = np.zeros((2,3),3)

# All ones
np.ones((4, 2, 2), dtype='int32')

# Any other number
np.full((2,2), 99, dtype='float32')

# Any other number (full_like)
np.full_like(a, 4)

# Random decimals
np.random.rand(4,2,3)
np.random.random_sample(a.shape)

# Random ints
np.random.randint(4,8, size=(3,3))

# Identity of matrix
np.identity(5)

# Repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis = 0)