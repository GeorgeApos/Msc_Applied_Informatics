#include <stdio.h>

int main1() {
    int i, j, n;
    printf("Enter the value of N: ");
    scanf("%d", &n);

    // Construct matrix A
    double A[n][n+1]; // Increased size to accommodate additional column
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (i == j) {
                A[i][j] = 4;  // Diagonal elements
            } else if (i - j == 1) {
                A[i][j] = 1;  // Elements below diagonal
            } else if (j - i == 1) {
                A[i][j] = 2;  // Elements above diagonal
            } else {
                A[i][j] = 0;  // Other elements
            }
        }
        A[i][n] = 1; // Assigning 1 to the additional column
    }

    // Print matrix A
    printf("\nMatrix A:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j <= n; j++) { // Modified loop bounds to print additional column
            printf("%.2f ", A[i][j]);
        }
        printf("\n");
    }

    /* generation of upper triangular matrix*/
    for (j = 0; j <= n; j++)
    {
        for (i = j + 1; i < n; i++)
        {
            double c = A[i][j] / A[j][j];
            for (int k = j; k <= n; k++)
            {
                A[i][k] = A[i][k] - c * A[j][k];
            }
        }
    }

    // Print upper triangular matrix
    printf("\nUpper Triangular Matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j <= n; j++) { // Modified loop bounds to print additional column
            printf("%.2f ", A[i][j]);
        }
        printf("\n");
    }

    /* backward substitution*/
    double x[n], sum;
    x[n-1] = A[n-1][n] / A[n-1][n-1];
    for (i = n - 2; i >= 0; i--)
    {
        sum = 0;
        for (j = i + 1; j < n; j++)
        {
            sum = sum + A[i][j] * x[j];
        }
        x[i] = (A[i][n] - sum) / A[i][i];
    }

    // Print the solution
    printf("\nSolution:\n");
    for (i = 0; i < n; i++) {
        printf("x%d = %.2f\n", i+1, x[i]);
    }

    return 0;
}
