//
// Created by Administrator on 2026/10/29.
//
#include <stdio.h>
int main() {
    int zx ;
    int zy ;
    int mx ;
    int my ;

    int block[25][25] = {0};
    long long dp [25][25] = {0};

    scanf("%d %d %d %d",&zx,&zy,&mx,&my);

    zx +=2;
    zy +=2;
    mx +=2;
    my +=2;

    block[mx][my] = 1;

    block[mx - 2][my - 1] = 1;
    block[mx - 2][my + 1] = 1;
    block[mx - 1][my - 2] = 1;
    block[mx - 1][my + 2] = 1;
    block[mx + 1][my - 2] = 1;
    block[mx + 1][my + 2] = 1;
    block[mx + 2][my - 1] = 1;
    block[mx + 2][my + 1] = 1;

    dp[2][2]=1;

    for (int i = 2; i < 25; i++) {
        for (int j = 2; j < 25; j++) {
            if (i==2&&j==2) continue;
            if (block[i][j] == 1) continue;
            dp [i] [j] = dp[i-1][j]+dp[i][j-1];

        }
    }
printf("%lld\n",dp[zx][zy]);



return 0;
}