import numpy as np

def gaussian_elimination(A, n):
    # Generation of upper triangular matrix
    for j in range(n):
        for i in range(j + 1, n):
            c = A[i][j] / A[j][j]
            A[i] = A[i] - c * A[j]

    # Backward substitution
    x = np.zeros(n)
    x[n-1] = A[n-1][n] / A[n-1][n-1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += A[i][j] * x[j]
        x[i] = (A[i][n] - sum) / A[i][i]

    return x

if __name__ == "__main__":
    n = 3
    A = np.array([[9, 3, 4, 7],
                        [4, 3, 4, 8],
                        [1, 1, 1, 3]], dtype=float)

    x = gaussian_elimination(A, n)

    print("\nThe solution is: ")
    for i in range(n):
        print(f"x{i} = {x[i]:.6f}")


# Explanation:
#
# Initialization:
# A is the augmented matrix representing the system of linear equations.
# n is the order of the matrix (number of unknowns).
#
# Gaussian Elimination:
# Convert the matrix A to upper triangular form. This involves iterating over each column and making all elements below the diagonal zero using row operations.
#
# Backward Substitution:
# Solve for the variables starting from the last row and moving upwards. The solution x is obtained by back substitution.
#
# Function Definition:
# The gaussian_elimination function performs the Gaussian elimination and backward substitution.
#
# Main Execution:
# The augmented matrix A is defined.
# The gaussian_elimination function is called with A and n.
#     The solution x is printed.