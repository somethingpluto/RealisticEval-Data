function countNumbers(str: string): number {
    let numberCount = 0;

    for (let i = 0; i < str.length; i++) {
        if (str[i] >= '0' && str[i] <= '9') {
            numberCount++;
        }
    }

    return numberCount;
}