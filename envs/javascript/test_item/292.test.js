/**
 * Calculate the remaining payment for a loan based on the given debt, monthly interest rate, and total payments.
 *
 * @param {number} principal - The initial amount of the debt.
 * @param {number} interestRate - The monthly interest rate as a decimal.
 * @param {number} numberOfPayments - The total number of payments.
 * @returns {number} - The calculated remaining payment.
 */
function calculateRemainingPayment(principal, interestRate, numberOfPayments) {
    // Calculate the monthly payment using the formula for a fixed-rate loan
    const monthlyPayment = principal * (interestRate * Math.pow(1 + interestRate, numberOfPayments)) / (Math.pow(1 + interestRate, numberOfPayments) - 1);

    // Calculate the total amount paid after all payments
    const totalPaid = monthlyPayment * numberOfPayments;

    // Calculate the remaining payment by subtracting the principal from the total paid
    const remainingPayment = totalPaid - principal;

    return remainingPayment;
}
describe('calculateRemainingPayment', () => {
  test('calculates remaining balance for typical loan conditions', () => {
    expect(calculateRemainingPayment(10000, 0.005, 24)).toBeCloseTo(0);
  });

  test('calculates remaining balance for high interest rate', () => {
    expect(calculateRemainingPayment(10000, 0.1, 12)).toBeCloseTo(0);
  });

  test('calculates remaining balance for low interest rate', () => {
    expect(calculateRemainingPayment(10000, 0.001, 60)).toBeCloseTo(0);
  });

  test('calculates remaining balance for very short term', () => {
    expect(calculateRemainingPayment(10000, 0.005, 1)).toBeCloseTo(0);
  });


  test('calculates remaining balance with no payments', () => {
    expect(calculateRemainingPayment(10000, 0.005, 0)).toBeCloseTo(10000);
  });

  test('calculates remaining balance for a long term', () => {
    expect(calculateRemainingPayment(10000, 0.005, 360)).toBeCloseTo(0);
  });
});
