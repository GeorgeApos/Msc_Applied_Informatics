import numpy as np


def gauss_seidel(A, b, x0, eps=1e-10, max_iters=1000):
    n = len(b)
    x = np.copy(x0)
    x_new = np.zeros_like(x)
    iters = 0
    error = np.inf

    while error > eps and iters < max_iters:
        for i in range(n):
            sum_ = 0.0
            for j in range(n):
                if j != i:
                    sum_ += A[i, j] * x_new[j]
            x_new[i] = (b[i] - sum_) / A[i, i]

        error = np.max(np.abs(x_new - x))
        x[:] = x_new  # Update x to x_new for the next iteration
        iters += 1

    if iters == max_iters:
        print("Maximum iterations reached without convergence.")
    else:
        print(f"Converged in {iters} iterations with error {error:.10f}.")

    return x


# Example usage
if __name__ == "__main__":
    A = np.array([
        [5, 6, 0, 4],
        [6, 8, 3, 1],
        [0, 3, 9, -1],
        [4, 1, -1, 12]
    ])

    b = np.array([-9, 5, 7, 11])
    x0 = np.zeros_like(b)  # Initial guess for x

    # Solve using Gauss-Seidel method
    x_solution = gauss_seidel(A, b, x0)

    # Print the solution vector x
    print("The solution vector x:")
    for i in range(len(x_solution)):
        print(f"x{i + 1} = {x_solution[i]}")
