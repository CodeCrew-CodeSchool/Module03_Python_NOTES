// this file was just made to test out the shorthand comparison operator to express a conditional range for the value of n
// in your terminal, simply run 
//      a
// this will execute the compiled executable of this code.

// If you want to practice writing your own C code, you'll need to install a compiler like gcc, clang, or zig (it's compiler is called zigcc)
// The way you compile a C program is to run
// like->   compilerName filename.c
//      gcc test.c

#include <stdio.h>

int main() {
    int n = 3;
    if (2 <= n <= 5) {
        printf("ok");
    }
}