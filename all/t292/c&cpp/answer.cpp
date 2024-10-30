#include <cmath>

double calculateRemainingPayment(double principal, double interestRate, int numberOfPayments) {
    double monthlyPayment = principal * (interestRate * pow(1 + interestRate, numberOfPayments)) / (pow(1 + interestRate, numberOfPayments) - 1);
    double balance = principal;
    for (int i = 0; i < numberOfPayments; i++) {
        balance = balance * (1 + interestRate) - monthlyPayment;
    }
    return balance;
}