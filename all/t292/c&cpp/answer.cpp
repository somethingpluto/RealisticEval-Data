#include <cmath>

double calculateRemainingPayment(double principal, double interestRate, int numberOfPayments) {
    // Calculate the fixed monthly payment using the amortization formula
    double monthlyPayment = principal * (interestRate * pow(1 + interestRate, numberOfPayments)) / (pow(1 + interestRate, numberOfPayments) - 1);

    // Calculate the remaining balance after all payments
    double balance = principal;
    for (int i = 0; i < numberOfPayments; i++) {
        balance = balance * (1 + interestRate) - monthlyPayment;
    }

    // Remaining balance after the payments
    return balance;
}