function countDashes(str: string): number {
    let dashCount = 0;

    for (let i = 0; i < str.length; i++) {
        if (str[i] === '-') {
            dashCount++;
        }
    }

    return dashCount;
}