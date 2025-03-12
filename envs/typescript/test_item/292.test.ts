import { validateNumber } from './validator'; // Assuming the validator module is in the same directory

function calculateRemainingPayment(
    principal: number,
    interestRate: number,
    numberOfPayments: number
): number {
    validateNumber(principal, 'principal');
    validateNumber(interestRate, 'interestRate');
    validateNumber(numberOfPayments, 'numberOfPayments');

    const monthlyPayment = principal * interestRate / (1 - Math.pow(1 + interestRate, -numberOfPayments));
    const paidInterest = principal * Math.pow(1 + interestRate, numberOfPayments) - principal;
    const remainingPrincipal = principal - (monthlyPayment * numberOfPayments - paidInterest);

    return remainingPrincipal;
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
