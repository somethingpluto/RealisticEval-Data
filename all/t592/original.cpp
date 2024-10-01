//Most of this code was written by ChatGPT
//It didn't a good lob but didn't quire works
//I think I have corrected it but user beware!!

#include <iostream>
#include <iostream>
#include <stack>
#include <string>
#include <cmath>

using namespace std;

int precedence(char op) {
    if (op == '+' || op == '-') {
        return 1;
    }
    if (op == '*' || op == '/') {
        return 2;
    }
    if (op == '^') {
        return 3;
    }
    return 0;
}

double applyOp(double a, double b, char op) {
    switch (op) {
    case '+': return a + b;
    case '-': return a - b;
    case '*': return a * b;
    case '/': return a / b;
    case '^': return pow(a, b);
    }
    return 0;
}