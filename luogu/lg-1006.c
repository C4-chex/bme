#include <stdio.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int a[55][55];       // 存储好心程度
int dp[110][55][55]; // dp[k][x1][x2] 表示第k步时两人分别在第x1, x2行的最大值

int main() {
    int m, n;
    // 读取行数和列数
    if (scanf("%d %d", &m, &n) != 2) return 0;

    // 读取矩阵数据
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    // 初始化 dp 数组为 0 (因为是求最大值，且好心程度都是非负数，初始0即可)
    // 如果担心越界问题，可以将整个数组初始化为极小值，但这里由于边界判断，0是安全的

    // k 表示当前走过的总步数（即 x + y 的值）
    // 起点 (1,1) 的 k 为 2，终点 (m,n) 的 k 为 m+n
    for (int k = 2; k <= m + n; k++) {
        // x1 是第一个人所在的行
        for (int x1 = 1; x1 <= m; x1++) {
            // y1 是第一人所在的列，必须保证在 1~n 之间
            int y1 = k - x1;
            if (y1 < 1 || y1 > n) continue;

            // x2 是第二个人所在的行
            for (int x2 = 1; x2 <= m; x2++) {
                // y2 是第二人所在的列，必须保证在 1~n 之间
                int y2 = k - x2;
                if (y2 < 1 || y2 > n) continue;

                // 当前两人所在格子的好心程度之和
                int current_val = a[x1][y1];
                // 如果两人不在同一个格子，则加上第二个人的好心程度
                if (x1 != x2) {
                    current_val += a[x2][y2];
                }

                // 状态转移：两人都有两种走法（向下走行数+1，向右走行数不变）
                // 对于上一步（k-1步），可能来自以下四种情况：
                // 1. 两人上一步都是向下走过来的 (x1-1, x2-1)
                // 2. 第一个人向下，第二个人向右 (x1-1, x2)
                // 3. 第一个人向右，第二个人向下 (x1, x2-1)
                // 4. 两人上一步都是向右走过来的 (x1, x2)

                int best_prev = dp[k-1][x1-1][x2-1]; // 下，下
                best_prev = MAX(best_prev, dp[k-1][x1-1][x2]); // 下，右
                best_prev = MAX(best_prev, dp[k-1][x1][x2-1]); // 右，下
                best_prev = MAX(best_prev, dp[k-1][x1][x2]);   // 右，右

                // 当前状态 = 上一步的最大值 + 当前格子的值
                dp[k][x1][x2] = best_prev + current_val;
            }
        }
    }

    // 最终答案是两人同时走到终点 (m,n) 时的状态
    // 此时 k = m+n, x1 = m, x2 = m
    printf("%d\n", dp[m+n][m][m]);

    return 0;
}