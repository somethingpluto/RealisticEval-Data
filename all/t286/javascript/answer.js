function findLargestDivisible(n) {
    let halfN = Math.floor(n / 2);

    for(let i = n; i >= halfN; i--) {
        if(i % 10 === 0 || i % 5 === 0) {
            return i;
        }
    }

    return null;
}