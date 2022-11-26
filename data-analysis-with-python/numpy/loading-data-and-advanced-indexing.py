import numpy as np
# Miscellaneous

## Load data from file
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int8')
print(filedata)

## Boolean Maskign and Advanced indexing
filedata > 50
filedata[filedata > 50]

np.any(filedata>50, axis=0)
np.all(filedata>50, axis=0)
np.all(filedata>50, axis=1)

((filedata > 50) & (filedata < 100))
(~((filedata > 50)) & (filedata < 100))


## You can index with a list in numpy
a = np.array([1,2,3,4,5,6,7,8,9])
a[[1,2,8]]