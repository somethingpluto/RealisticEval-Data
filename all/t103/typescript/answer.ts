const truncateStringWithReplacement = (str: string, maxLength: number): string => {
    // Check if the string length is less than or equal to the specified length
    if (str.length <= maxLength) {
        return str; // No need to truncate
    }

    // Replace the excess part with ellipsis
    return str.slice(0, maxLength) + '...';
};