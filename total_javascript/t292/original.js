/**
 * 
 * @param {number} debt 
 * @param {number} monthlyInterestRate 
 * @param {number} totalPayments 
 * @returns 
 */
const calculateRemainingPayment = (debt, monthlyInterestRate, totalPayments) => {
    return (debt * monthlyInterestRate) /
      (1 - Math.pow(1 + monthlyInterestRate, -totalPayments));
  }