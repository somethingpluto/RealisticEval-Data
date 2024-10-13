def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculates the Body Mass Index (BMI) based on weight and height.

    The BMI is calculated using the formula:
        BMI = weight (kg) / (height (m) * height (m))

    :param weight: The weight of the individual in kilograms.
    :param height: The height of the individual in meters.

    :return: The calculated BMI value as a float.

    :raises InvalidInputError: If weight or height is less than or equal to zero,
                               since these values must be positive.
    """
    # Validate weight and height
    if weight <= 0:
        raise Exception("Weight must be greater than zero.")
    if height <= 0:
        raise Exception("Height must be greater than zero.")

    # Calculate BMI
    bmi = weight / (height * height)
    return bmi  # Return the calculated BMI value