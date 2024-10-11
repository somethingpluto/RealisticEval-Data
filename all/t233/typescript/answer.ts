function removeComments(inputString: string): string {
    // Use regular expression to match lines starting with '#'
    return inputString.replace(/#.*/g, '');
}