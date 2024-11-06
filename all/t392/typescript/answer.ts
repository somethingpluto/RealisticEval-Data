function lookAndSay(number: string): string {
    let result: string[] = [];
    let count: number = 1;
    const length: number = number.length;
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