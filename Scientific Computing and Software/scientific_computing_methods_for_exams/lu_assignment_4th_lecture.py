import numpy as np


def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i, i] = 1.0

    for i in range(n):
        for k in range(i, n):
            sum_ = sum(L[i, j] * U[j, k] for j in range(i))
            U[i, k] = A[i, k] - sum_

        for k in range(i, n):
            if i != k:
                sum_ = sum(L[k, j] * U[j, i] for j in range(i))
                L[k, i] = (A[k, i] - sum_) / U[i, i]

    return L, U


def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]

    return y


def back_substitution(U, y):
    n = len(y)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    return x


if __name__ == "__main__":
    A = np.array([
        [3, -7, -2, 2],
        [-3, 5, 1, 0],
        [6, -4, 0, -5],
        [-9, 5, -5, 12]
    ])

    b = np.array([-9, 5, 7, 11])

    # Perform LU decomposition
    L, U = lu_decomposition(A)

    # Solve Ly = b using forward substitution
    y = forward_substitution(L, b)

    # Solve Ux = y using back substitution
    x = back_substitution(U, y)

    # Print the solution vector x
    print("The solution vector x:")
    for i in range(len(x)):
        print(f"x{i + 1} = {x[i]}")
