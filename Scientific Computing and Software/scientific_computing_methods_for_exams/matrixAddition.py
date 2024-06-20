import multiprocessing as mp
import time

N = 20
a = [0] * N
b = [1] * N
c = [1] * N


def add_elements(i):
    return b[i] + c[i]


if __name__ == '__main__':
    no_procs = mp.cpu_count()
    print(f"Available processors: {no_procs}")

    start_time = time.time()

    with mp.Pool(processes=1) as pool:
        a = pool.map(add_elements, range(N))

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f}")

    for i in range(N):
        print(f"a[{i}]={a[i]}")

# Explanation:

# Initialization: The N, a, b, and c arrays are initialized similarly to the C code.
# Function Definition: A function add_elements is defined to add corresponding elements of b and c.
# Multiprocessing Pool: A pool of workers is created using multiprocessing.Pool.
# Parallel Execution: The pool.map function is used to parallelize the addition operation across multiple processes.
# Timing: The execution time is measured using time.time().
# Printing Results: The results are printed similarly to the C code.