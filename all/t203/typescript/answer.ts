function reverseRange(v: number[], a: number, b: number): void {
    if (a < 0 || b >= v.length || a > b) {
        console.error("Invalid indices");
        return;
    }
    const subArray = v.slice(a, b + 1).reverse();
    for (let i = 0; i < subArray.length; i++) {
        v[a + i] = subArray[i];
    }
}