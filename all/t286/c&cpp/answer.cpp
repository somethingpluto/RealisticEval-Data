#include <iostream>
using namespace std;

// Function to find the largest integer between a given number n and half of it that is divisible by 10 or 5
int findLargestDivisible(int n) {
    // Iterate from n down to half of n
    for (int i = n; i >= n / 2; --i) {
        // Check if the number is divisible by 10 or 5
        if (i % 10 == 0 || i % 5 == 0) {
            return i;
        }
    }
    // Return -1 if no such number exists
    return -1;
}
