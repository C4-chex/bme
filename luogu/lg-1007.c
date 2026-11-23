#include<stdio.h>
int smin;
int smax=0;
int pmin=0;
int pmax=0;
int main() {
    int L;
    scanf("%d", &L);
    int N;
    scanf("%d", &N);
    int x;
    int i;
    for (i = 0; i < N; i++) {
        scanf("%d", &x);

        int xleft = x;
        int xright = L+1-x;

        pmin = (xleft < xright) ? xleft : xright;
        pmax = (xleft > xright) ? xleft : xright;

        smin = (pmin>smin) ? pmin : smin;
        smax = (pmax>smax) ? pmax : smax;



    }
    printf("%d %d\n", smin, smax);

    return 0;



}