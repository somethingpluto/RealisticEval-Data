function replacePhoneNumbers(text) {
    /**
     * Replace all phone numbers (in various formats) in the string with the string '[PHONE_NUM]'
     * For example:
     *      input: Call me at 123-456-7890.
     *      output: Call me at [PHONE_NUM].
     *
     * @param {string} text - The input string that may contain phone numbers.
     * @returns {string} - The modified string with phone numbers replaced by '[PHONE_NUM]'.
     */
    
    // Regular expression to match various phone number formats
    const phoneRegex = /(\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b)|(\b\d{10}\b)/g;
    
    return text.replace(phoneRegex, '[PHONE_NUM]');
}