import numpy as np

# Define two 2D vectors as 1D NumPy arrays
v = np.array([3, 4])
w = np.array([5, -2])

# Vector addition and subtraction
v_plus_w = v + w
v_minus_w = v - w

# Print results
print('v = ', v)
print('w = ', w)
print('v + w =', v_plus_w)
print('v + w =', v_minus_w)
