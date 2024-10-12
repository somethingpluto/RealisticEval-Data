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
    # Calculate the fixed monthly payment using the amortization formula
    monthly_payment = principal * (interest_rate * (1 + interest_rate) ** number_of_payments) / \
                      ((1 + interest_rate) ** number_of_payments - 1)

    # Calculate the remaining balance after all payments (assuming all payments are made)
    balance = principal
    for _ in range(number_of_payments):
        balance = balance * (1 + interest_rate) - monthly_payment

    # Remaining balance after the payments
    return balance