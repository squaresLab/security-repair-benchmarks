//
// Created by Jyoti Prakash on 25.03.21.
//

#include <limits.h>
int foo(int, int);

void bar(int);

int main() {
    int x = INT_MAX, y = 7;
    int z = foo(x, y);
    bar(z);
}

void bar(int x) {
    x = 6;
}

int foo(int x, int y) {
    y=y+1;
    return x+y;
}


