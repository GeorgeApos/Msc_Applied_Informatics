import numpy as np


def cholesky_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            sum_ = sum(L[i, k] * L[j, k] for k in range(j))
            if i == j:
                L[i, j] = np.sqrt(A[i, i] - sum_)
            else:
                L[i, j] = (1.0 / L[j, j] * (A[i, j] - sum_))
    return L


def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]
        y[i] /= L[i, i]

    return y


def back_substitution(L_T, y):
    n = len(y)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= L_T[i, j] * x[j]
        x[i] /= L_T[i, i]

    return x


if __name__ == "__main__":
    A = np.array([
        [5, 6, 0, 4],
        [6, 8, 3, 1],
        [0, 3, 9, -1],
        [4, 1, -1, 12]
    ])

    b = np.array([-9, 5, 7, 11])

    # Perform Cholesky decomposition
    L = cholesky_decomposition(A)

    # Solve Ly = b using forward substitution
    y = forward_substitution(L, b)

    # Solve L^T x = y using back substitution
    L_T = np.transpose(L)
    x = back_substitution(L_T, y)

    # Print the solution vector x
    print("The solution vector x:")
    for i in range(len(x)):
        print(f"x{i + 1} = {x[i]}")
