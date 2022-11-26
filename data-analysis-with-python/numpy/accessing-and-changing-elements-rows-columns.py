import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print("Array:", a)

# Get specific element [r, c]
print("Index [1,5]: ", a[1, 5])

# Get specific row
print("Row 0: ", a[0, :])

# Get specific coulomb
print("Coulomb 2: ", a[:,2])

# More fancy [startindex:endindex:stepsize]
print("Fancy: ", a[0, 1:6:2])

# Change element
a[1,5] = 20
print("Changed a[1,5]: ", a)
a[:, 2] = [1, 2]
print("Changed coloumb 2: ", a)