import numpy as np

def f1(x1, x2):
    arg = 10 * x1 - x2**2 - 8
    if arg < 0:
        return 0.1  # Εναλλακτική τιμή για την αποφυγή αρνητικών τιμών κάτω από τη ρίζα
    else:
        return np.sqrt(arg)

def f2(x1, x2):
    arg = 10 * x2 - x1 * x2**2 - 8
    if arg < 0 or x1 == 0:
        return 0.1  # Εναλλακτική τιμή για την αποφυγή αρνητικών τιμών κάτω από τη ρίζα ή x1 = 0
    else:
        return (np.sqrt(arg) - 1) / x1

def fixed_point_iteration(x0, tolerance=1e-5, max_iterations=1000):
    x = np.array(x0, dtype=float)
    x_prev = np.zeros_like(x)
    iterations = 0
    error = float('inf')

    while error > tolerance and iterations < max_iterations:
        x[0] = f1(x[0], x[1])
        x[1] = f2(x[0], x[1])

        error = np.max(np.abs(x - x_prev))
        x_prev[:] = x
        iterations += 1

    if iterations == max_iterations:
        print(f"Maximum iterations {max_iterations} reached. Solution may not be accurate.")
    else:
        print(f"Converged in {iterations} iterations.")

    return x

def main():
    x0 = [0.1, 0.1]
    tolerance = 1e-5

    print(f"Solving with fixed point iteration method...")
    solution = fixed_point_iteration(x0, tolerance)

    print(f"Solution: x1 = {solution[0]}, x2 = {solution[1]}")

if __name__ == "__main__":
    main()
