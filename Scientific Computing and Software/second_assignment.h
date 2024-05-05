#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

int N;

double jacobi_over_relaxation(bool method, double A[N][N], double b[N], double x[N], double omega, double tolerance) {
    double x_new[N];
    double error;
    int i, j, iter = 0;

    do {
        for (i = 0; i < N; i++) {
            double sigma = 0.0;
            for (j = 0; j < N; j++) {
                if (j != i) {
                    sigma += A[i][j] * x[j];
                }
            }
            x_new[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sigma);
        }

        error = 0.0;
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

double successive_over_relaxation(bool method, double A[N][N], double b[N], double x[N], double omega, double tolerance) {
    double x_new[N];
    double error;
    int i, j, iter = 0;

    do {
        for (i = 0; i < N; i++) {
            double sum1 = 0.0, sum2 = 0.0;
            for (j = 0; j < i; j++) {
                sum1 += A[i][j] * x[j]; // Use x instead of x_new
            }
            for (j = i + 1; j < N; j++) {
                sum2 += A[i][j] * x[j];
            }
            x_new[i] = (1 - omega) * x[i] + (omega / A[i][i]) * (b[i] - sum1 - sum2);
        }

        error = 0.0;
        for (i = 0; i < N; i++) {
            double diff = fabs(x_new[i] - x[i]);
            if (diff > error) {
                error = diff;
            }
            x[i] = x_new[i];
        }

        iter++;
    } while (error > tolerance);

    if (!method) {
        printf("Successive Over-Relaxation: Converged in %d iterations\n", iter);
    }

    return iter;
}


double find_optimal_omega(double A[N][N], double b[N], double x[N], double tolerance) {
    double min_iter = INFINITY;
    double optimal_omega;

    for (double omega = 0.1; omega <= 2.0; omega += 0.1) {
        double iter_jacobi = jacobi_over_relaxation(true, A, b, x, omega, tolerance);
        double iter_sor = successive_over_relaxation(true, A, b, x, omega, tolerance);

        if (iter_jacobi < min_iter) {
            min_iter = iter_jacobi;
            optimal_omega = omega;
        }
        if (iter_sor < min_iter) {
            min_iter = iter_sor;
            optimal_omega = omega;
        }
    }

    return optimal_omega;
}

int main2() {
    printf("Enter the value of N: ");
    scanf("%d", &N);

    double A[N][N];
    double b[N]; // Removed initialization
    double x[N]; // Removed initialization
    double omega = 1.2; // Change this to experiment with different values of omega
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

    jacobi_over_relaxation(false, A, b, x, omega, tolerance);

    printf("Solution using Jacobi Over-Relaxation:\n");
    for (int i = 0; i < N; i++) {
        printf("x[%d] = %f\n", i, x[i]);
    }

    printf("\n");

    successive_over_relaxation(false, A, b, x, omega, tolerance);

    printf("Solution using Successive Over-Relaxation:\n");
    for (int i = 0; i < N; i++) {
        printf("x[%d] = %f\n", i, x[i]);
    }

    double optimal_omega = find_optimal_omega(A, b, x, tolerance);
    printf("Optimal omega: %f\n", optimal_omega);

    return 0;
}
