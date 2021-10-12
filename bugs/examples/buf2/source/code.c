#include <stdio.h>

void bad() {
  int x = 5600;
  int arr[] = {0, 2, 4, 6, 8};
  int val = arr[x];
  printf("index %d = %d", x, val);
}

int main() {
  bad();
}
