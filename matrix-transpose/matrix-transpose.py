import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    A = np.asarray(A)
    rows, cols = A.shape
    A_transposed = np.zeros(shape=(cols, rows))
    for col in range(0, cols):
        for row in range(0, rows):
            A_transposed[col, row] = A[row, col]

    return A_transposed
            
