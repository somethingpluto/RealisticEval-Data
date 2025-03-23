

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == False
    assert candidate([1, 2, -3, 1, 2, -3]) == False
    assert candidate([1, 2, -4, 5, 6]) == True
    assert candidate([1, -1, 2, -2, 5, -5, 4, -4]) == False
    assert candidate([1, -1, 2, -2, 5, -5, 4, -5]) == True
    assert candidate([1, -2, 2, -2, 5, -5, 4, -4]) == True

from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.

    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    count = 0
    while balance < 0:
        if any(move_amount_to_zero_in_account(operations[0]) for move_amount_to_zero_in_account(operations[0])):
            print(f"Account balance: {balance}, falling below zero")
            balance += operations[0]
            count += 1
        else:
            if balance < 0:
                print(f"Account balance: {balance}, falling below zero")
                balance += operations[0]
                count += 1
    return count == len(operations)

candidate = below_zero
check(candidate)