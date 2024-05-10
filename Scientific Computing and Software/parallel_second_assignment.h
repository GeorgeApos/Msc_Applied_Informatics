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
        #pragma omp parallel for private(j) shared(A, b, x, x_new) // Distribute loop iterations across threads
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
        }

        error = 0.0;
        #pragma omp parallel for reduction(max:error) // Combine maximum errors from all threads
        for (i = 0; i < N; i++) {
            double diff = fabs(x_new[i] - x[i]);
            if (diff > error) {
                error = diff;
            }
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
        #pragma omp parallel for private(j) shared(A, b, x, x_new) // Distribute loop iterations across threads
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
        }

        error = 0.0;
        #pragma omp parallel for reduction(max:error) // Combine maximum errors from all threads
        for (i = 0; i < N; i++) {
            double diff = fabs(x_new[i] - x[i]);
            if (diff > error) {
                error = diff;
            }
            x[i] = x_new[i];
        }

        iter++;
    } while (error > tolerance && iter < 1000);

    if(!method) {
        printf("Successive Over-Relaxation: Converged in %d iterations\n", iter);
    }

    return iter;
}

int main3() {
    double (*A)[N] = malloc(N * sizeof(double[N])); // Allocate memory for A
    double *b = malloc(N * sizeof(double)); // Allocate memory for b
    double *x = malloc(N * sizeof(double)); // Allocate memory for x
    double tolerance = 1e-7;
    int sizes[] = {1000, 10000, 20000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    if (A == NULL || b == NULL || x == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (int k = 0; k < num_sizes; k++) {
        int current_size = sizes[k];

        // Construct the A matrix
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


        double start_time = omp_get_wtime(); // Start timing

        double jac_iter = par_jacobi_over_relaxation(false, A, b, x, 1, tolerance);

        double end_time = omp_get_wtime(); // End timing
        double jac_elapsed_time = end_time - start_time;

        printf("Solution using Parallel Jacobi Over-Relaxation for size %d:\n", current_size);
        for (int i = 0; i < current_size; i++) {
            printf("x[%d] = %f\n", i, x[i]);
        }
        printf("Jacobi Over-Relaxation: Converged in %f iterations\n", jac_iter);
        printf("Elapsed time: %f seconds\n", jac_elapsed_time);

        printf("\n");

        start_time = omp_get_wtime(); // Start timing

        double sor_iter = par_successive_over_relaxation(false, A, b, x, 1, tolerance);

        end_time = omp_get_wtime(); // End timing
        double sor_elapsed_time = end_time - start_time;

        printf("Solution using Successive Parallel Over-Relaxation for size %d:\n", current_size);
        for (int i = 0; i < current_size; i++) {
            printf("x[%d] = %f\n", i, x[i]);
        }
        printf("Successive Over-Relaxation: Converged in %f iterations\n", sor_iter);
        printf("Elapsed time: %f seconds\n", sor_elapsed_time);

        double optimal_omega = compute_optimal_omega(A);
        printf("Optimal omega for size %d: %f\n\n", current_size, optimal_omega);
    }

    free(A);
    free(b);
    free(x);

    return 0;
}
