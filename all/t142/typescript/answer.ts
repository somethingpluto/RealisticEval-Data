function camelCaseToCapitalizedWithSpaces(input: string): string {
    // Use a regular expression to insert spaces before capital letters and numbers
    const spacedString = input.replace(/([A-Z0-9])/g, ' $1');

    // Capitalize the first letter of each word
    const capitalizedString = spacedString
        .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');

    // Trim any leading spaces and return the model_result
    return capitalizedString.trim();
}