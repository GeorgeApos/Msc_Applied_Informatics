import numpy as np


def power_iteration(A, x_old, eps=1e-4, max_iters=1000):
    n = len(A)
    x = np.array(x_old)
    iters = 0

    while True:
        y = np.dot(A, x)  # Multiplication A*x_old

        maxValue = np.max(np.abs(y))  # Compute max norm of vector y
        x = y / maxValue  # Normalize vector y and update x

        error = np.max(np.abs(x - x_old))  # Compute error
        x_old = np.array(x)

        iters += 1
        print(f"Iteration: {iters}, approximate eigenvalue: {maxValue:.10f}")

        if iters >= max_iters or error < eps:
            break

    return maxValue


if __name__ == "__main__":
    A = np.array([[-261, 209, -49],
                  [-530, 422, -98],
                  [-800, 631, -144]], dtype=float)
    x_old = np.array([1, 1, 1], dtype=float)

    eigenvalue = power_iteration(A, x_old)

    print("\nThe dominant eigenvalue is:", eigenvalue)

# Explanation:
#
# Initialization:
# A is the matrix for which we want to find the dominant eigenvalue.
# x_old is the initial guess for the eigenvector associated with the dominant eigenvalue.
#
# Power Iteration Function (power_iteration):
# Performs the power iteration method to find the dominant eigenvalue of matrix A.
# Iterates until convergence criteria are met (max_iters iterations or eps error tolerance).
#
# Multiplication A*x_old:
# Computes the matrix-vector multiplication A * x_old.
#
# Compute Max Norm of Vector y:
# Finds the maximum absolute value in vector y.
#
# Normalize Vector y and Update x:
# Normalizes vector y by dividing by its maximum absolute value to get x, the eigenvector estimate for the dominant eigenvalue.
#
# Compute Error:
# Calculates the error by finding the maximum absolute difference between x and x_old.
#
# Update x_old:
# Updates x_old with the current x for the next iteration.
#
# Main Execution:
# Initializes matrix A and vector x_old.
# Calls power_iteration function to compute the dominant eigenvalue and prints it.
#
# Notes:
#
# This Python code uses NumPy for efficient matrix operations and handling of arrays.
# The power iteration method is used to iteratively refine the estimate of the dominant eigenvalue and its associated eigenvector.
# Adjust the matrix A and initial vector x_old according to your specific problem to find the dominant eigenvalue of different matrices.
