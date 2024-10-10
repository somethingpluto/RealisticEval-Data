function probabilityOfRedBalls(n, x, y) {
    // calculate combinations
    const combination = (n, k) => {
        let result = 1;
        for(let i = 0; i < k; i++) {
            result *= (n - i);
            result /= (i + 1);
        }
        return result;
    }

    // calculate probability
    const totalBalls = x + y;
    const numerator = combination(x, n) * combination(y, totalBalls - n);
    const denominator = combination(totalBalls, n);

    return numerator / denominator;
}