import numpy as np
import multiprocessing as mp
import time

N = 5000

# Initialize matrices
a = np.ones((N, N), dtype=int)
b = np.ones((N, N), dtype=int)
c = np.zeros((N, N), dtype=int)


def matrix_multiply(row):
    result_row = np.zeros(N, dtype=int)
    for j in range(N):
        for k in range(N):
            result_row[j] += a[row, k] * b[k, j]
    return result_row


if __name__ == '__main__':
    no_procs = mp.cpu_count()
    print(f"Available processors: {no_procs}")

    start_time = time.time()

    # Create a pool of workers
    with mp.Pool(processes=12) as pool:
        result = pool.map(matrix_multiply, range(N))

    # Convert list of rows to a full matrix
    c = np.array(result)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f}")

# If you want to print the result matrix, you can uncomment the lines below
# for i in range(N):
#     print(f"c[{i}]= {c[i]}")

# Explanation:

# Initialization:
#     a and b are initialized to be matrices filled with ones.
#         c is initialized to be a matrix filled with zeros.
#
# Function Definition:
# matrix_multiply(row): This function calculates the product of a single row from matrix a with matrix b and returns the resulting row. This mimics the inner loops of matrix multiplication.
#
# Multiprocessing:
# A pool of workers is created with mp.Pool(processes=12) to utilize 12 parallel processes.
# pool.map(matrix_multiply, range(N)) is used to apply the matrix_multiply function to each row of matrix a in parallel.
#
# Timing:
# Execution time is measured using time.time().
#
# Conversion of Results:
# The result from pool.map is a list of rows which is then converted back to a full matrix using np.array(result).
#
# Notes:
#
# Python's multiprocessing library does not work exactly like OpenMP, but it allows for parallel execution of tasks.
# The use of NumPy for matrix operations ensures efficient handling of large arrays.
# The if __name__ == '__main__': block is necessary to safely create the pool of workers, especially when running the script on Windows.
# The actual printing of the matrix c has been commented out to avoid flooding the console with output, but you can uncomment it if needed.