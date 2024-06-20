import numpy as np

def max_norm(x1, x2):
    return np.max(np.abs(x1 - x2))

def jacobi_iteration(A, b, x_old, max_iters=100, eps=1e-7):
    n = len(b)
    x_new = np.zeros_like(x_old)
    iters = 0
    error = eps + 1  # Start with an error larger than eps

    while error > eps and iters < max_iters:
        for i in range(n):
            sum_ = np.dot(A[i, :], x_old) - A[i, i] * x_old[i]
            x_new[i] = (b[i] - sum_) / A[i, i]

        error = max_norm(x_old, x_new)
        x_old[:] = x_new  # Update x_old with x_new for the next iteration
        iters += 1

    return x_new, iters

if __name__ == "__main__":
    n = 9  # Size of the matrix A
    m = 4  # Number used for setting up co-diagonals in A

    A = np.zeros((n, n))
    b = np.array([-2, -1, -2, -1, 0, -1, -2, -1, -2])
    x_old = np.zeros(n)

    # Setup matrix A
    for i in range(n):
        A[i, i] = -4

    for i in range(n - 1):
        if (i + 1) % (m - 1) != 0:
            A[i, i + 1] = 1
            A[i + 1, i] = 1

    for i in range(n - m + 1):
        A[i, i + m - 1] = 1
        A[i + m - 1, i] = 1

    print("Matrix A:")
    print(A)

    # Solve using Jacobi method
    solution, iterations = jacobi_iteration(A, b, x_old)

    print("\nRequired number of iterations for convergence:", iterations)

    print("\nThe solution is:")
    for i in range(n):
        print(f"x{i} = {solution[i]:.10f}")

    input()  # To keep the console open after execution

# Explanation:

# The Jacobi method is an iterative method for solving linear systems of equations. It is based on splitting the matrix A into a diagonal component D and the remaining components R. The iteration formula for the Jacobi method is given by:
# x_new = D^(-1) * (b - R * x_old)
# where x_new is the updated solution, x_old is the previous solution, D is the diagonal component of A, and R is the remaining components of A. The method iteratively updates the solution until a convergence criterion is met.
# In this code, we define a function jacobi_iteration that implements the Jacobi method for solving a linear system of equations Ax = b. The function takes as input the matrix A, the vector b, an initial guess x_old, the maximum number of iterations, and the convergence criterion eps.
# The function initializes x_new as an array of zeros and iterates until the convergence criterion is met or the maximum number of iterations is reached. In each iteration, it updates x_new using the Jacobi iteration formula and calculates the error between x_old and x_new.
# The code also includes a test case where we define a 9x9 matrix A and a vector b, and solve the linear system using the Jacobi method. The solution and the number of iterations required for convergence are printed to the console.
# The code demonstrates how to implement the Jacobi method for solving linear systems of equations and provides an example of solving a specific linear system using the method. The Jacobi method is a simple iterative method that can be used for solving large sparse linear systems efficiently.
