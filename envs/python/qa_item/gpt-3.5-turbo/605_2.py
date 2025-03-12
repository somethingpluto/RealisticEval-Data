import math

def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculates the Body Mass Index (BMI) based on weight and height.
    Args:
        weight (float): The weight of the individual in kilograms.
        height (float): The height of the individual in meters.

    Returns:
        float: The calculated BMI value as a float.
    """
    return weight / math.pow(height, 2)
import unittest


class Tester(unittest.TestCase):

    # Test case for valid inputs with expected BMI value
    def test_valid_bmi_calculations(self):
        # Normal weight
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, delta=0.01)  # 70 kg, 1.75 m

        # Underweight
        self.assertAlmostEqual(calculate_bmi(50, 1.75), 16.33, delta=0.01)  # 50 kg, 1.75 m

        # Overweight
        self.assertAlmostEqual(calculate_bmi(80, 1.75), 26.12, delta=0.01)  # 80 kg, 1.75 m

        # Obesity
        self.assertAlmostEqual(calculate_bmi(100, 1.75), 32.65, delta=0.01)  # 100 kg, 1.75 m

    # Test case for invalid inputs
    def test_invalid_bmi_calculations(self):
        # Negative weight
        with self.assertRaises(Exception) as context:
            calculate_bmi(-70, 1.75)

        # Zero height
        with self.assertRaises(Exception) as context:
            calculate_bmi(70, 0)

        # Negative height
        with self.assertRaises(Exception) as context:
            calculate_bmi(70, -1.75)

if __name__ == '__main__':
    unittest.main()