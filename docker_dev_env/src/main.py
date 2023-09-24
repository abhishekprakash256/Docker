"""
The main file of the docker image 

"""

import numpy as np 

arr = np.array([1, 2, 3, 4, 5])

print(arr)

count = 0 
while count < 200:
	print(count)
	count +=1