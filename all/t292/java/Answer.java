package org.real.temp;

/**
 * Calculate the remaining payment for a loan based on the given debt, monthly interest rate, and total payments.
 *
 * @param principal - The initial amount of the debt.
 * @param interestRate - The monthly interest rate as a decimal.
 * @param numberOfPayments - The total number of payments.
 * @return - The calculated remaining payment.
 */
public class Answer {
    public static double calculateRemainingPayment(double principal, double interestRate, int numberOfPayments) {
        // Calculate the fixed monthly payment using the amortization formula
        double monthlyPayment = principal * (interestRate * Math.pow(1 + interestRate, numberOfPayments)) / 
                                 (Math.pow(1 + interestRate, numberOfPayments) - 1);
        
        // Calculate the remaining balance after all payments
        double balance = principal;
        for (int i = 0; i < numberOfPayments; i++) {
            balance = balance * (1 + interestRate) - monthlyPayment;
        }

        // Remaining balance after the payments
        return balance;
    }
}