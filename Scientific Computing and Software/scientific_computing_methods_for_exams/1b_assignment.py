import numpy as np

def jacobi_method(A, b, x0, tolerance=1e-7, max_iterations=1000):
    n = len(b)
    x = np.copy(x0)
    x_new = np.zeros_like(x)
    iterations = 0
    error = float('inf')

    while error > tolerance and iterations < max_iterations:
        for i in range(n):
            sigma = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - sigma) / A[i, i]

        error = np.max(np.abs(x_new - x))
        x[:] = x_new
        iterations += 1

    return x, iterations

def successive_over_relaxation(A, b, x0, omega, tolerance=1e-7, max_iterations=1000):
    n = len(b)
    x = np.copy(x0)
    x_new = np.zeros_like(x)
    iterations = 0
    error = float('inf')

    while error > tolerance and iterations < max_iterations:
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - sum1 - sum2)

        error = np.max(np.abs(x_new - x))
        x[:] = x_new
        iterations += 1

    return x, iterations

def main():
    sizes = [1000, 10000, 20000]
    tolerance = 1e-7

    for current_size in sizes:
        A = np.zeros((current_size, current_size))
        b = np.ones(current_size)
        x0 = np.zeros(current_size)

        # Construct A matrix (tridiagonal with specific values)
        for i in range(current_size):
            for j in range(current_size):
                if i == j:
                    A[i, j] = 4.0
                elif abs(i - j) == 1:
                    A[i, j] = -1.0

        # Solve with Jacobi method
        print(f"Solving with Jacobi method for size {current_size}...")
        x_jacobi, iter_jacobi = jacobi_method(A, b, x0, tolerance)
        print(f"Jacobi method: Converged in {iter_jacobi} iterations.")

        # Solve with Successive Over-Relaxation (SOR)
        omega = 1.5  # You can adjust omega based on your needs
        print(f"Solving with SOR method for size {current_size}...")
        x_sor, iter_sor = successive_over_relaxation(A, b, x0, omega, tolerance)
        print(f"SOR method with omega={omega}: Converged in {iter_sor} iterations.")

        print("\n")

if __name__ == "__main__":
    main()
