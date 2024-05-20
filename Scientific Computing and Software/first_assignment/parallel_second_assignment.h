#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <omp.h>

#define N 20000

double par_jacobi_over_relaxation(bool method, double A[N][N], double b[N], double x[N], double omega, double tolerance) {
    double x_new[N];
    double error;
    int i, j, iter = 0;

    do {
        error = 0.0;
        #pragma omp parallel for private(i, j) shared(x_new, x, A, b) reduction(max:error)
        for (i = 0; i < N; i++) {
            double sigma = 0.0;
            for (j = 0; j < N; j++) {
                if (j != i) {
                    sigma += A[i][j] * x[j];
                }
            }

            if (A[i][i] == 0) {
                x_new[i] = 0;
            } else {
                x_new[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sigma);
            }

            double diff = fabs(x_new[i] - x[i]);
            if (diff > error) {
                error = diff;
            }
        }

        #pragma omp parallel for
        for (i = 0; i < N; i++) {
            x[i] = x_new[i];
        }

        iter++;
    } while (error > tolerance);

    if(!method) {
        printf("Jacobi Over-Relaxation: Converged in %d iterations\n", iter);
    }

    return iter;
}

double par_successive_over_relaxation(bool method, double A[N][N], double b[N], double x[N], double omega, double tolerance) {
    double x_new[N];
    double error;
    int i, j, iter = 0;

    do {
        error = 0.0;
        #pragma omp parallel for private(i, j) shared(x_new, x, A, b) reduction(max:error)
        for (i = 0; i < N; i++) {
            double sum1 = 0.0, sum2 = 0.0;
            for (j = 0; j < i; j++) {
                sum1 += A[i][j] * x_new[j];
            }
            for (j = i + 1; j < N; j++) {
                sum2 += A[i][j] * x[j];
            }

            if(A[i][i] == 0){
                x_new[i] = 0;
            } else {
                x_new[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sum1 - sum2);
            }

            double diff = fabs(x_new[i] - x[i]);
            if (diff > error) {
                error = diff;
            }
        }

        #pragma omp parallel for
        for (i = 0; i < N; i++) {
            x[i] = x_new[i];
        }

        iter++;
    } while (error > tolerance && iter < 1000);

    return iter;
}

int main3() {
    double (*A)[N] = malloc(N * sizeof(double[N])); // Allocate memory for A
    double *b = malloc(N * sizeof(double)); // Allocate memory for b
    double *x = malloc(N * sizeof(double)); // Allocate memory for x
    double tolerance = 1e-7;
    int sizes[] = {1000, 10000, 20000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
    int num_cores[] = {1, 2, 4, 8}; // Adjust according to available cores
    int num_core_sizes = sizeof(num_cores) / sizeof(num_cores[0]);

    if (A == NULL || b == NULL || x == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (int k = 0; k < num_sizes; k++) {
        int current_size = sizes[k];

        // Construct the A matrix
        #pragma omp parallel for
        for (int i = 0; i < current_size; i++) {
            for (int j = 0; j < current_size; j++) {
                if (i == j) {
                    A[i][j] = 4.0; // Initialize diagonal elements to 4.0
                } else if (abs(i - j) == 1) {
                    A[i][j] = -1.0; // Initialize off-diagonal elements to -1.0
                } else {
                    A[i][j] = 0.0; // Initialize all other elements to 0.0
                }
            }
            b[i] = 1.0; // Initialize b to 1.0
            x[i] = 0.0; // Initialize x to 0.0
        }

        double serial_time_jac, parallel_time_jac;
        double serial_time_sor, parallel_time_sor;

        // Jacobi Over-Relaxation Serial
        double start_time = omp_get_wtime(); // Start timing
        jacobi_over_relaxation(false, A, b, x, 1, tolerance);
        serial_time_jac = omp_get_wtime() - start_time; // End timing

        // Successive Over-Relaxation Serial
        start_time = omp_get_wtime(); // Start timing
        successive_over_relaxation(false, A, b, x, 1, tolerance);
        serial_time_sor = omp_get_wtime() - start_time; // End timing

        for (int c = 0; c < num_core_sizes; c++) {
            int cores = num_cores[c];
            omp_set_num_threads(cores);

            // Jacobi Over-Relaxation Parallel
            start_time = omp_get_wtime(); // Start timing
            par_jacobi_over_relaxation(false, A, b, x, 1, tolerance);
            parallel_time_jac = omp_get_wtime() - start_time; // End timing

            double speedup_jac = serial_time_jac / parallel_time_jac;
            double efficiency_jac = speedup_jac / cores;

            printf("Jacobi Over-Relaxation for size %d with %d cores: Speedup = %f, Efficiency = %f\n",
                   current_size, cores, speedup_jac, efficiency_jac);

            // Successive Over-Relaxation Parallel
            start_time = omp_get_wtime(); // Start timing
            par_successive_over_relaxation(false, A, b, x, 1, tolerance);
            parallel_time_sor = omp_get_wtime() - start_time; // End timing

            double speedup_sor = serial_time_sor / parallel_time_sor;
            double efficiency_sor = speedup_sor / cores;

            printf("Successive Over-Relaxation for size %d with %d cores: Speedup = %f, Efficiency = %f\n",
                   current_size, cores, speedup_sor, efficiency_sor);
        }

        double optimal_omega = compute_optimal_omega(true, A, b, x, tolerance);
        printf("Optimal omega for size %d: %f\n\n", current_size, optimal_omega);
    }

    free(A);
    free(b);
    free(x);

    return 0;
}
