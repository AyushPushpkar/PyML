import numpy as np


# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

print(arr_1d[1])
print(arr_1d[-2])

arr_2d = np.array([[1, 2, 3], [4, 5, 6] , [7 , 8 ,9]])
print(arr_2d[1,2])
print(arr_2d[0,-1])

print(arr_2d[1])  # row 
print(arr_2d[:,0]) # column

boolean_index = arr_2d[(arr_2d > 3) & (arr_2d < 8)]
print(boolean_index)

print(arr_2d[0,[0,2]]) # int array indexing

slice_1d = arr_1d[1:4]
print("\n",slice_1d)
slice_1d = arr_1d[0:5 :2]
print(slice_1d)

slice_2d = arr_2d[:2 , :2]
print("\n",slice_2d)

rows_2d = arr_2d[:1]
print(rows_2d)

column_2d = arr_2d[: , -1]
print("\n",column_2d)

step_rows_2d = arr_2d[::2]
print("\n",step_rows_2d)

step_col2d = arr_2d[: , ::2]
print("\n" , step_col2d)