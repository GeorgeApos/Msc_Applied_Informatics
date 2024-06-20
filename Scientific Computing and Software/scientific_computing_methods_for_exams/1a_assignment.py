import numpy as np

def solve_system(A, b):
    n = len(b)
    x = np.zeros(n, dtype=float)

    # Forward elimination (Gaussian elimination with partial pivoting)
    for i in range(n):
        # Partial pivoting
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k, i]) > abs(A[max_row, i]):
                max_row = k
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Elimination step
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Back substitution
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

def main():
    n = int(input("Enter the value of N: "))

    A = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i, j] = 4.0
            elif i - j == 1:
                A[i, j] = 1.0
            elif j - i == 1:
                A[i, j] = 2.0

    b = np.ones(n, dtype=float)

    print("\nMatrix A:")
    print(A)

    x = solve_system(A, b)

    print("\nSolution:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.2f}")

if __name__ == "__main__":
    main()
