#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <omp.h>

int N;

double par_jacobi_over_relaxation(bool method, double A[N][N], double b[N], double x[N], double omega, double tolerance) {
    double x_new[N];
    double error = 0.0;
    int i, j, iter = 0;

    do {
        #pragma omp parallel for private(j) shared(A, b, x, x_new)
        for (i = 0; i < N; i++) {
            double sigma = 0.0;
            for (j = 0; j < N; j++) {
                if (j != i) {
                    sigma += A[i][j] * x[j];
                }
            }
            x_new[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sigma);
            double diff = fabs(x_new[i] - x[i]);
            if (diff > error) {
                error = diff;
            }
        }

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

double parallel_successive_over_relaxation(bool method, double A[N][N], double b[N], double x[N], double omega, double tolerance) {
    double x_new[N];
    double error;
    int i, j, iter = 0;

    do {
        #pragma omp parallel for private(j) shared(A, b, x, x_new)
        for (i = 0; i < N; i++) {
            double sum1 = 0.0, sum2 = 0.0;
            for (j = 0; j < i; j++) {
                sum1 += A[i][j] * x_new[j];
            }
            for (j = i + 1; j < N; j++) {
                sum2 += A[i][j] * x[j];
            }
            x_new[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sum1 - sum2);
            double diff = fabs(x_new[i] - x[i]);
            if (diff > error) {
                error = diff;
            }
        }

        for (i = 0; i < N; i++) {
            x[i] = x_new[i];
        }

        iter++;
    } while (error > tolerance && iter < 1000);

    if (!method) {
        printf("Successive Over-Relaxation: Converged in %d iterations\n", iter);
    }

    return iter;
}

int main3() {
    printf("Enter the value of N: ");
    scanf("%d", &N);

    double A[N][N];
    double b[N]; // Removed initialization
    double x[N]; // Removed initialization
    double optimal_omega = compute_optimal_omega(A);
    double tolerance = 1e-7;

    // Construct the A matrix
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) {
                A[i][j] = 4;
            } else if (abs(i - j) == 1) {
                A[i][j] = -1;
            } else {
                A[i][j] = 0;
            }
        }
        b[i] = 1; // Initialize b to 1
        x[i] = 0; // Initialize x to 0
    }

    double start_time = omp_get_wtime();
    par_jacobi_over_relaxation(false, A, b, x, optimal_omega, tolerance);
    double end_time = omp_get_wtime();
    printf("Jacobi Over-Relaxation Execution Time: %.6f seconds\n", end_time - start_time);

    printf("Solution using Jacobi Over-Relaxation:\n");
    for (int i = 0; i < N; i++) {
        printf("x[%d] = %f\n", i, x[i]);
    }

    printf("\n");

    start_time = omp_get_wtime();
    parallel_successive_over_relaxation(false, A, b, x, optimal_omega, tolerance);
    end_time = omp_get_wtime();
    printf("Successive Over-Relaxation Execution Time: %.6f seconds\n", end_time - start_time);

    printf("Solution using Successive Over-Relaxation:\n");
    for (int i = 0; i < N; i++) {
        printf("x[%d] = %f\n", i, x[i]);
    }

    printf("Optimal omega: %f\n", optimal_omega);

    return 0;
}
