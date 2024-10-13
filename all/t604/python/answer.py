def power_tail(x: int, y: int, acc: int = 1) -> int:
    if y == 0:
        return acc  # Return accumulated result

    # Tail-recursive call with decremented exponent and updated accumulator
    return power_tail(x, y - 1, acc * x)
