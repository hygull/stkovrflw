import numpy as np 
from copy import deepcopy

array = np.zeros(10)
arrays = []

for i in range(len(array)):
	array[i] = 1
	arrays.append(deepcopy(array))

print(arrays)
# [array([1., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), array([1., 1., 0., 0., 0., 0., 0., 0., 0., 0.]), array([1., 1., 1., 0., 0., 0., 0., 0., 0., 0.]), array([1., 1., 1., 1., 0., 0., 0., 0., 0., 0.]), array([1., 1., 1., 1., 1., 0., 0., 0., 0., 0.]), array([1., 1., 1., 1., 1., 1., 0., 0., 0., 0.]), array([1., 1., 1., 1., 1., 1., 1., 0., 0., 0.]), array([1., 1., 1., 1., 1., 1., 1., 1., 0., 0.]), array([1., 1., 1., 1., 1., 1., 1., 1., 1., 0.]), array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])]

print(arrays[0])
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

print(arrays[-1])
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
