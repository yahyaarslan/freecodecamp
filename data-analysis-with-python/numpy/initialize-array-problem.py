import numpy as np

a = np.ones((5, 5), dtype='int8')

a[1:-1,1:-1] = 0

a[2,2] = 9
print(a)