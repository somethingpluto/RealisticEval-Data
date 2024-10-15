/**
 * Checks whether the provided password meets the specified format requirements:
 * - At least one number
 * - At least one lowercase letter
 * - At least one uppercase letter
 * - At least one punctuation mark
 * - Minimum length of 8 characters
 *
 * @param {string} password - The password string to validate
 * @returns {boolean} Returns true if the password meets all requirements; otherwise, false.
 */
function isValidPassword(password: string): boolean {
    // Regular expression patterns for the required criteria
    const hasNumber = /[0-9]/;                          // At least one number
    const hasLowercase = /[a-z]/;                       // At least one lowercase letter
    const hasUppercase = /[A-Z]/;                       // At least one uppercase letter
    const hasPunctuation = /[!@#$%^&*(),.?":{}|<>]/;   // At least one punctuation mark
    const hasMinimumLength = /.{8,}/;                   // At least 8 characters

    // Check each condition
    const isValid = hasNumber.test(password) &&
                    hasLowercase.test(password) &&
                    hasUppercase.test(password) &&
                    hasPunctuation.test(password) &&
                    hasMinimumLength.test(password);

    return isValid;
}