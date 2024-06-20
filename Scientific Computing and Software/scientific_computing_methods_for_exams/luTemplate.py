import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        L[j][j] = 1.0  # Diagonal elements of L are 1
        for i in range(j+1):
            sum_upper = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - sum_upper
        for i in range(j, n):
            sum_lower = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = (A[i][j] - sum_lower) / U[j][j]

    return L, U

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]

    return y

def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x

if __name__ == "__main__":
    A = np.array([[3, -7, -2, 2],
                  [-3, 5, 1, 0],
                  [6, -4, 0, -5],
                  [-9, 5, -5, 12]], dtype=float)
    b = np.array([[-7, 6, 1, -7]], dtype=float).T  # Transpose to make it a column vector

    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)

    print("\nThe solution is: ")
    for i in range(len(x)):
        print(f"x{i} = {x[i]:.10f}")

# Explanation:
#
# LU Decomposition Function (lu_decomposition):
# Computes the LU decomposition of matrix A.
# Updates matrices L (lower triangular) and U (upper triangular) such that A = LU.
#
# Forward Substitution Function (forward_substitution):
# Solves the system Ly = b using forward substitution to find y.
#
# Backward Substitution Function (backward_substitution):
# Solves the system Ux = y using backward substitution to find x, which is the solution to the original system Ax = b.
#
# Main Execution:
# Initializes matrix A and vector b.
# Calls lu_decomposition to compute L and U.
# Calls forward_substitution to solve Ly = b and obtain y.
# Calls backward_substitution to solve Ux = y and obtain x, which is printed as the solution.
#
# Notes:
#
# Ensure that NumPy (import numpy as np) is installed in your Python environment (pip install numpy if not).
# The solution x is printed using formatted output (f-string) to display it with high precision.
# Adjust the matrix A and vector b according to your specific system of linear equations.