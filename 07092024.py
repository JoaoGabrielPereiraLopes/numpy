import numpy as np

# arrayi8: 5D array with shape (1, 2, 1, 3, 1)
arrayi8 = np.array([[x for x in range(1, 4)]*2], dtype='i1', ndmin=5)
print(arrayi8.shape)   # (1, 2, 1, 3, 1)
print(arrayi8.dtype)   # int8
print(arrayi8)         # [[[1], [2], [3]], [[1], [2], [3]]]
print()

# Reshape arrayi8 into (6,1)
newarrayi8 = arrayi8.reshape(6, 1)
print(newarrayi8)
print()

# arrayi1: 5D array with shape (3, 1, 2, 1, 1)
arrayi1 = np.array([[0, 2], [0, 0], [1, 1]], dtype='i1', ndmin=5)
print(arrayi1.shape)   # (3, 1, 2, 1, 1)
print(arrayi1.dtype)   # int8
print(arrayi1)         # Structure with (0,2), (0,0), and (1,1)
print()

# arr: 3D array reshaped from 1D array to (2, 3, 2)
arr = np.array([x for x in range(1, 13)]) # to 2, 3, 2
arr = arr.reshape(2, 3, 2)
print(arr, '\n')

# 3x3 array
array = np.array([x for x in range(1, 10)])
array = array.reshape(3, 3)
print(array)

# Array filled with 'vazio' reshaped to 3x3
print(np.array(['vazio' for x in range(9)]).reshape(3, -1), '\n')

# Flattening arr to 1D array
print(arr.reshape(-1), '\n')

# Iterating over arrayi1 with nditer and converting to string (op_dtypes='S')
for x in np.nditer(arrayi1, flags=['buffered'], op_dtypes='S'):
    print(x)
print()

# Iterating and enumerating a 1D array
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(f'{idx[0]}:{x}')
print()

# Iterating and enumerating a 2D array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(f'{idx[1]} {idx[0]}:{x}')

# Concatenating two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
print()

# Concatenating 5D arrays
concatenated=np.concatenate((arrayi1.reshape(2,3), arrayi8.reshape(2,3)))
new_array=np.array(concatenated,ndmin=5)
print(new_array,'\n')

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr,'\n')

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)