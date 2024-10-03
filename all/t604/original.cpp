// This program is written by ChatGPT4, after I prompted the
// required message in README and then asked it to propose
// me a tail recursive function

#include <stdio.h>

// acc is to store the accumulating result
unsigned power_tail(unsigned x, unsigned y, unsigned acc) {
  // base case
  if (y == 0) {
    return acc;
  }

  // tail-recursive
  return power_tail(x, y - 1, x * acc);
}

// wrap function
unsigned power(unsigned x, unsigned y) {
  return power_tail(x, y, 1);
}