function compressWhitespace(inputString: string): string {
    // Split the input string by whitespace and join with a single space
    return inputString.split(/\s+/).join(' ');
}