function countDashes(str) {
    let dashCount = 0;

    for (let i = 0; i < str.length; i++) {
        if (str[i] === '-') {
            dashCount++;
        }
    }

    return dashCount;
}
