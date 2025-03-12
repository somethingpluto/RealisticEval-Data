def calculate_remaining_payment(principal: float, interest_rate: float, number_of_payments: int) -> float:
    """
    Calculate the remaining payment for a loan based on the given debt, monthly interest rate, and total payments.

    Args:
        principal (float): The initial amount of the debt.
        interest_rate (float): The monthly interest rate as a decimal.
        number_of_payments (int): The total number of payments.

    Returns:
        float: The calculated remaining payment.
    """
    if number_of_payments == 0:
        return principal
    else:
        monthly_payment = principal * (interest_rate / (1 - (1 + interest_rate) ** -number_of_payments))
        remaining_payment = principal * (1 + interest_rate) ** number_of_payments - (monthly_payment / interest_rate) * ((1 + interest_rate) ** number_of_payments - 1)
        return remaining_payment
import unittest


class TestCalculateRemainingPayment(unittest.TestCase):

    def test_typical_loan_conditions(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 24), 0, places=2)

    def test_high_interest_rate(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.1, 12), 0, places=2)

    def test_low_interest_rate(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.001, 60), 0, places=2)

    def test_very_short_term(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 1), 0, places=2)

    def test_no_payments(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 0), 10000, places=2)

    def test_long_term(self):
        self.assertAlmostEqual(calculate_remaining_payment(10000, 0.005, 360), 0, places=2)

if __name__ == '__main__':
    unittest.main()