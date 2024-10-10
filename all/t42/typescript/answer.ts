function replacePhoneNumbers(text: string): string {
    /**
     * Replace all phone numbers (phone formats in many) in the string with the string [PHONE_NUM].
     * For example:
     *      Input: Call me at 123-456-7890.
     *      Output: Call me at [PHONE_NUM].
     *
     * @param {string} text - The input string that may contain phone numbers.
     * @returns {string} - The modified string with phone numbers replaced by '[PHONE_NUM]'.
     */

    // Regex pattern to match various phone number formats
    const phoneRegex = /(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}/g;

    return text.replace(phoneRegex, '[PHONE_NUM]');
}