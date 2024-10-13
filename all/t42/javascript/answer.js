function replacePhoneNumbers(text) {
    // Define a regex pattern to match phone numbers
    // This pattern matches optional country codes, spaces, dashes, and brackets commonly found in phone numbers
    const phonePattern = /\b(?:\+\d{1,2}\s?)?(\d{1,4}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,9}[-.\s]?\d{1,9}\b/g;

    // Replace all matches in the text with [PHONE_NUM]
    const replacedText = text.replace(phonePattern, '[PHONE_NUM]');

    return replacedText;
}