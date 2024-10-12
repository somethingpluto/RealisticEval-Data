def get_array_average(array):
    sum_ = 0
    for i in range(len(array)):
        sum_ += array[i]
    return sum_ / len(array) if array else 0  # Avoid division by zero
