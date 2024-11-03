/**
 * Calculates the Body Mass Index (BMI) given weight and height.
 *
 * @param {number} weight - The weight in kilograms, must be greater than zero.
 * @param {number} height - The height in meters, must be greater than zero.
 * @return {number} The calculated BMI value.
 * @throws {Error} Throws an error if weight or height is less than or equal to zero.
 */
function calculateBMI(weight: number, height: number): number {
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