import numpy as np

# 0D array (scalar)
arr_0d = np.array(42)

print("0D array:", arr_0d)
print("Shape:", arr_0d.shape)   # ()
print("Dimensions:", arr_0d.ndim)  # 0

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

print("1D array:", arr_1d)
print("Shape:", arr_1d.shape)   # (5,)
print("Dimensions:", arr_1d.ndim)  # 1
print(arr_1d.dtype)
print(arr_1d.size)


# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# 3D array
arr_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr_3d)


# Create a 3x3 array filled with zeros
zeros_array = np.zeros((3, 3))

# Create a 2x4 array filled with ones
ones_array = np.ones((2, 4))

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)

# Create a 1D array from range
range_array = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Create an array with random numbers
random_array = np.random.rand(2, 3)  # 2x3 array with values in [0, 1)

linspace_array = np.linspace(0,2,5) # Generates num evenly spaced values between start and stop, inclusive.

randint = np.random.randint(3, 10 , (2,3)) # between 2 and 3 , 2x3 matrix
