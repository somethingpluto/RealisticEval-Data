def scale_to_range(input_array, input_min, input_max, output_min, output_max):
    # Ensure all values in input_array are within the input range
    for value in input_array:
        if value < input_min or value > input_max:
            raise ValueError(f"Value {value} in input_array is outside the range [{input_min}, {input_max}].")

    scale = (output_max - output_min) / (input_max - input_min)

    # Scale the input array
    return [(value - input_min) * scale + output_min for value in input_array]
