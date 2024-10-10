#include <iostream>
using namespace std;

double factorial(int num)
{
    if(num == 0 || num == 1)
        return 1;
    else
        return num * factorial(num - 1);
}

double probabilityRedBalls(int x, int n, int m)
{
    double numerator = factorial(n) / (factorial(x) * factorial(n-x));
    double denominator = factorial(m+n) / (factorial(m) * factorial(n));

    return numerator / denominator;
}
