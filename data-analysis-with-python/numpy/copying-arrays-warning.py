# Be careful when copying arrays
a = np.array([1,2,3])
b = a
b[0] = 100 # a[0] = 100

# To prevent
a = np.array([1,2,3])
b = a.copy
b[0] = 100 
