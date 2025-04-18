/**
 * Hides the sensitive part of a bank account number with 17 numbers, only showing the last 4 characters.
 *
 * @param {string} account - The bank account number to hide.
 * @returns {string} - The bank account number with the first part hidden.
 * @throws {Error} - Throws an error if the account number is not exactly 17 characters long.
 */
function hideBankAccount(account) {
    // Validate that the account number is exactly 17 characters long
    if (account.length !== 17) {
        throw new Error("Account number must be exactly 17 characters long.");
    }

    // Create the hidden representation with "****" prefix
    const hiddenPart = "****";

    // Extract the visible part of the account number (last 4 characters)
    const visiblePart = account.substring(13); // Get last 4 characters

    // Return the formatted string with hidden and visible parts
    return hiddenPart + visiblePart;
}