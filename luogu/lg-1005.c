
#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int a[81][81];

    // 输入矩阵
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    // 计算每次取数的权重
    long long w[81];
    w[0] = 1;

    for (int i = 1; i <= m; i++) {
        w[i] = w[i-1] * 2;
    }

    long long ans = 0;

    // 逐行处理
    for (int row = 1; row <= n; row++) {

        long long dp[81][81] = {0};

        // 遍历当前行的所有状态
        for (int l = 0; l <= m; l++) {
            for (int r = 0; r <= m-l; r++) {

                if (l + r == m) {
                    continue;
                }

                int step = l + r + 1;

                // 尝试从左边取
                long long score =
                    dp[l][r] + (long long)a[row][l+1] * w[step];

                if (score > dp[l+1][r]) {
                    dp[l+1][r] = score;
                }

                // 尝试从右边取
                score =
                    dp[l][r] + (long long)a[row][m-r] * w[step];

                if (score > dp[l][r+1]) {
                    dp[l][r+1] = score;
                }
            }
        }

        // 找到当前行的最大得分
        long long best = 0;

        for (int l = 0; l <= m; l++) {
            if (dp[l][m-l] > best) {
                best = dp[l][m-l];
            }
        }

        ans += best;
    }

    printf("%lld\n", ans);

    return 0;
}
