/**
 * Calculate the remaining payment for a loan based on the given debt, monthly interest rate, and total payments.
 *
 * @param {number} principal - The initial amount of the debt.
 * @param {number} interestRate - The monthly interest rate as a decimal.
 * @param {number} numberOfPayments - The total number of payments.
 * @returns {number} - The calculated remaining payment.
 */
function calculateRemainingPayment(
    principal: number,
    interestRate: number,
    numberOfPayments: number
): number {
    // Calculate the fixed monthly payment using the amortization formula
    const monthlyPayment = principal * (interestRate * Math.pow(1 + interestRate, numberOfPayments)) / (Math.pow(1 + interestRate, numberOfPayments) - 1);

    // Calculate the remaining balance after all payments (assuming all payments are made, should be very close to zero)
    let balance = principal;
    for (let i = 0; i < numberOfPayments; i++) {
        balance = balance * (1 + interestRate) - monthlyPayment;
    }

    // Remaining balance after the payments
    return balance;
}/**
 * Calculate the remaining payment for a loan based on the given debt, monthly interest rate, and total payments.
 *
 * @param {number} principal - The initial amount of the debt.
 * @param {number} interestRate - The monthly interest rate as a decimal.
 * @param {number} numberOfPayments - The total number of payments.
 * @returns {number} - The calculated remaining payment.
 */
function calculateRemainingPayment(
    principal: number,
    interestRate: number,
    numberOfPayments: number
): number {
    // Calculate the fixed monthly payment using the amortization formula
    const monthlyPayment = principal * (interestRate * Math.pow(1 + interestRate, numberOfPayments)) / (Math.pow(1 + interestRate, numberOfPayments) - 1);

    // Calculate the remaining balance after all payments (assuming all payments are made, should be very close to zero)
    let balance = principal;
    for (let i = 0; i < numberOfPayments; i++) {
        balance = balance * (1 + interestRate) - monthlyPayment;
    }

    // Remaining balance after the payments
    return balance;
}