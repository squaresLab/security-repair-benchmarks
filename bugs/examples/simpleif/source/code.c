#include <limits.h>

void bad() {
  int x = INT_MAX;
  int y = 7;
  int z = 4;
  if (z == 4 && (x > 0 || y > 0)) {
    z = x + y;
  }
}

int main() {
  bad();
}
