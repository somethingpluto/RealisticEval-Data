function lookAndSay(number) {
    /**
     * Generates the next sequence in the 'look-and-say' sequence by reading off the digits of the given number,
     * grouping by consecutive digits.
     *
     * @param {string} number - The current sequence as a string.
     * @returns {string} - The next sequence in the 'look-and-say' series.
     */
    let result = [];
    let count = 1;
    const length = number.length;

    // Iterate through the number, group by consecutive digits and count them
    for (let i = 1; i < length; i++) {
        if (number[i] === number[i - 1]) {
            count += 1;
        } else {
            result.push(`${count}${number[i - 1]}`);
            count = 1;
        }
    }

    // Append the last group of digits
    result.push(`${count}${number[length - 1]}`);

    return result.join('');
}