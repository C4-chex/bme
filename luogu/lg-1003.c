#include <math.h>
#include <stdbool.h>
#include <stdio.h>

#include <stdio.h>

// 1. 定义“地毯”结构体
struct Carpet {
    int x;
    int y;
    int w;
    int h;
};

int main() {
    int n;
    scanf("%d", &n);


    struct Carpet carpets[10005];

    for (int i = 1; i <= n; i++) {

        scanf("%d %d %d %d", &carpets[i].x, &carpets[i].y, &carpets[i].w, &carpets[i].h);


    }

    int tx, ty;
    scanf("%d %d", &tx, &ty);

    int ans = -1;
    
    for (int i = n; i >= 1; i--) {
        // 判断目标点是否在 carpets[i] 的范围内
        if (tx >= carpets[i].x && tx <= carpets[i].x + carpets[i].w &&
            ty >= carpets[i].y && ty <= carpets[i].y + carpets[i].h) {
            ans = i;
            break;
            }
    }

    printf("%d\n", ans);
    return 0;
}