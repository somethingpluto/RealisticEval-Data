########################################################################
# Generated by ChatGPT 3.5 on 2023-12-06 using the prompt
# "I am working on a programming problem. Can you come up
# with a solution in Python?" followed by the problem description
#
# I added the if __name__ == "__main__" block, but
# ``sum_calibration_values`` is untouched.
########################################################################


def sum_calibration_values(calibration_document):
    total_sum = 0

    for line in calibration_document:
        # Filter out non-digit characters
        digits = [char for char in line if char.isdigit()]

        # Extract the first and last digits
        if digits:
            first_digit = int(digits[0])
            last_digit = int(digits[-1])

            # Combine to form a two-digit number
            calibration_value = first_digit * 10 + last_digit

            # Add to the total sum
            total_sum += calibration_value

    return total_sum


if __name__ == "__main__":
    # Example calibration document
    with open("./input.txt") as f:
        calibration_document = f.readlines()

    # Calculate the sum of all calibration values
    result = sum_calibration_values(calibration_document)

    # Print the model_answer_result
    print(result)