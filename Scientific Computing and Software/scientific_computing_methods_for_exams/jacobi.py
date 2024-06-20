import numpy as np


def max_norm(x1, x2, n):
    return np.max(np.abs(x1 - x2))


def jacobi_method(A, b, x0, eps=1e-7, max_iters=100):
    n = len(b)
    x_old = x0
    x_new = np.zeros_like(x0)
    iters = 0

    while True:
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if i != j:
                    sum += A[i][j] * x_old[j]
            x_new[i] = (b[i] - sum) / A[i][i]

        iters += 1
        error = max_norm(x_old, x_new, n)
        x_old = x_new.copy()

        if error < eps or iters >= max_iters:
            break

    return x_new, iters


if __name__ == "__main__":
    n = 3
    A = np.array([[2, -1, 0],
                  [-1, 2, -1],
                  [0, -1, 2]], dtype=float)
    b = np.array([1, 0, 1], dtype=float)
    x0 = np.zeros(n)

    x, iters = jacobi_method(A, b, x0)

    print(f"\nRequired number of iterations for convergence: {iters}\n")

    print("\nThe solution is: ")
    for i in range(n):
        print(f"x{i} = {x[i]:.10f}")

# Explanation:
#
# Initialization:
# The matrices A and b are defined as NumPy arrays for efficient computation.
#     x0 is the initial guess for the solution.
#
# Function Definitions:
# max_norm: Calculates the maximum norm (infinity norm) between two vectors x1 and x2.
# jacobi_method: Implements the Jacobi iterative method to solve the system Ax = b.
#
# Jacobi Iteration:
# The method iterates over each row of A, computing the new values for x_new based on the previous values x_old.
# The max_norm function is used to determine the convergence by comparing x_new and x_old.
#
# Convergence Criteria:
# The iteration stops when the error (difference between x_new and x_old) is less than eps or the number of iterations exceeds max_iters.
#
# Main Execution:
# The jacobi_method function is called with the initialized values.
# The required number of iterations and the solution x are printed.