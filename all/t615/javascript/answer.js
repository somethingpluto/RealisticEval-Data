function calculate(values, period) {
    // Check if the number of values is less than the specified period
    if (!values || values.length < period || period <= 0) {
        return NaN;  // Return NaN for invalid input
    }

    let sumValues = 0.0;  // Initialize the sum

    // Calculate the sum of the last 'period' values
    for (let i = values.length - period; i < values.length; i++) {
        sumValues += values[i];
    }

    // Return the average of the last 'period' values
    return sumValues / period;
}