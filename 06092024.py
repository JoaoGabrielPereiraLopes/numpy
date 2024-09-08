import numpy as np

d0=np.array(42)#0-d
print(d0)
print(type(d0))
print(d0.ndim)
print(d0.dtype)
print('')

d1=np.array([1,2,3,4,5])#1-d
print(d1)
print(type(d1))
print(d1.ndim)
print(d1.dtype)
print('')

d2 = np.array([[1,2,3], [4,5,6]])#2-d
print(d2)
print(type(d2))
print(d2.ndim)
print(d2.dtype)
print('')

d3= np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(d3)
print(type(d3))
print(d3.ndim)
print(d3.dtype)
print('')

d5 = np.array([1, 2, 3, 4],dtype='i4', ndmin=5)
print(d5)
print(d5.dtype)
print('number of dimensions :', d5.ndim )

arrstr = np.array(['apple', 'banana', 'cherry'])
print(arrstr.dtype)
print()

d5=d5.astype('S')
print(d5)
print(d5.dtype)
print()

arr = np.array([1, 0, 0.5])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
print()

arr=np.array([1,2,3,4,5])
newarr=arr.view()
newarr[0]=2
print(arr,newarr)
print()

x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)