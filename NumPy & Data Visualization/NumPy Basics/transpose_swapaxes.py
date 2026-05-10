# transpose_swapaxes.py
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print('Original matrix:', matrix)
print('Transpose:', matrix.T)
print('Swap axes:', np.swapaxes(matrix, 0, 1))
