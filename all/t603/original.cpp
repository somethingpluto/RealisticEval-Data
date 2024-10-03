#include <stdio.h>

int main() {
    int year;
    printf("Enter a year: ");
    scanf("%d", &year);

    // Leap year if perfectly divisible by 400
    if (year % 400 == 0) {
        printf("%d is a leap year.\n", year);
    }
    // Not a leap year if divisible by 100 but not divisible by 400
    else if (year % 100 == 0) {
        printf("%d is not a leap year.\n", year);
    }
    // Leap year if not divisible by 100 but divisible by 4
    else if (year % 4 == 0) {
        printf("%d is a leap year.\n", year);
    }
    // All other years are not leap years
    else {
        printf("%d is not a leap year.\n", year);
    }

    return 0;
}
// Generated with copilot! https://copilot-language.github.io/