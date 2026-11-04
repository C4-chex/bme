#include <stdio.h>

int block[15][15] = {0};
int dp[15][15][15][15] = {0};

int max4(int a, int b, int c, int d) {
    int m = a > b ? a : b;
    m = m > c ? m : c;
    m = m > d ? m : d;
    return m;
}

int main() {
    int n, x, y, v;
    scanf("%d", &n);
    while (scanf("%d %d %d", &x, &y, &v) == 3) {
        if (x == 0 && y == 0 && v == 0) break;
        block[x][y] = v;
    }

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            for (int k = 1; k <= n; k++)
                for (int l = 1; l <= n; l++) {
                    dp[i][j][k][l] = max4(
                        dp[i-1][j][k-1][l],
                        dp[i-1][j][k][l-1],
                        dp[i][j-1][k-1][l],
                        dp[i][j-1][k][l-1]
                    ) + block[i][j] + block[k][l];
                    if (i == k && j == l)
                        dp[i][j][k][l] -= block[i][j];
                }

    printf("%d\n", dp[n][n][n][n]);
    return 0;
}