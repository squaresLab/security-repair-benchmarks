#include <stdio.h>

int main() {
    int x, check, z;
    int buf1[10], buf2[8];
    int *base = buf1;
    scanf("%d", &check);
    x = check + 1;
    z = *(buf1 + 8);
    int i = 0;
    while (i < check) {
        buf1[i] = i + 1;
        ++i;
    }

    i = 0;
    while (i < check) {
        buf2[i] = i + 1;
        ++i;
    }
}
