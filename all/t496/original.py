def generate_ith_row_pascal(i: int) -> list:
    """
    Generates the ith row of Pascal's Triangle. Written by GPT4 after user prompt: 'generate the ith row of Pascal's
    Triangle using inbuilt functions in python.'

    :param i: row number
    :return: list
    """
    return [int(comb(i, j)) for j in range(i + 1)]