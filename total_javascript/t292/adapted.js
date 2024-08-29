/**
 * Calculate the remaining payment for a loan based on the given debt, monthly interest rate, and total payments.
 *
 * @param {number} principal - The initial amount of the debt.
 * @param {number} interestRate - The monthly interest rate as a decimal.
 * @param {number} numberOfPayments - The total number of payments.
 * @returns {number} - The calculated remaining payment.
 */
const calculateRemainingPayment = (principal, interestRate, numberOfPayments) => {
    const numerator = principal * interestRate;
    const denominator = 1 - Math.pow(1 + interestRate, -numberOfPayments);
    return numerator / denominator;
}
