
function calculateBMI(weight, height) {
    // Validate weight and height
    if (weight <= 0) {
        throw new Error("Weight must be greater than zero.");
    }
    if (height <= 0) {
        throw new Error("Height must be greater than zero.");
    }

    // Calculate BMI
    const bmi = weight / (height * height);
    return bmi; // Return the calculated BMI value
}