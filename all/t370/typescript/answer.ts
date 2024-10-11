function decompose(n: number, shape: number[]): number[] {
    let result: number[] = [];
    let remaining = n;

    for(let i = shape.length - 1; i >= 0; i--) {
        if(remaining < 0 || remaining >= shape[i]) {
            throw new Error(`Index ${n} is out of bounds for shape ${shape}`);
        }

        result.unshift(remaining % shape[i]);
        remaining = Math.floor(remaining / shape[i]);
    }

    return result;
}