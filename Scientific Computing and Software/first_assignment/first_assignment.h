#include <stdio.h>

int main1() {
    int i, j, n;
    printf("Enter the value of N: ");
    scanf("%d", &n);

    double A[n][n+1];
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (i == j) {
                A[i][j] = 4;
            } else if (i - j == 1) {
                A[i][j] = 1;
            } else if (j - i == 1) {
                A[i][j] = 2;
            } else {
                A[i][j] = 0;
            }
        }
        A[i][n] = 1;
    }

    printf("\nMatrix A:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j <= n; j++) {
            printf("%.2f ", A[i][j]);
        }
        printf("\n");
    }

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

    printf("\nUpper Triangular Matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j <= n; j++) {
            printf("%.2f ", A[i][j]);
        }
        printf("\n");
    }

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

    printf("\nSolution:\n");
    for (i = 0; i < n; i++) {
        printf("x%d = %.2f\n", i+1, x[i]);
    }

    return 0;
}
