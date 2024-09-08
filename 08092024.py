import numpy as np

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 6)
for x in newarr:
    print(x)
print()

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3,axis=0)
for x in newarr:
    print(x,'\n')

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
for x in newarr:
    print(x)
print()

newarr=np.array(newarr).reshape(arr.shape)
print(newarr,'\n'*2,arr,end='\n'*2)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
select = np.where(arr == 4)
for x in select:
    print(x)
print()

sequenci=np.array([x for x in range(1000)])
perfect_squares=np.array(np.where((sequenci**(1/2))%1==0))
for x in perfect_squares.reshape(-1):
    print(f'{int(sequenci[x]**(1/2))} : {sequenci[x]}')
print()

arr = np.array([6, 7, 8, 9, 7])
x = np.searchsorted(arr, 7)
print(x,end='\n'*2)

arr = np.array([1, 2, 3, 4, 5, 6])
for x in arr:
    if is_prime(x):
        print('arr tem primos')
        break
print()

arr = np.array([6,7,8,9])
x = np.searchsorted(arr, 7, side='right')
print(x,end='\n'*2)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x,end='\n'*2)