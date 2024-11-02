class OrthogonalPolynomial {
    alpha: number;
    beta: number;
    gamma: number;
    quadratureRule: QuadratureRule;

    constructor(alpha: number, beta: number, gamma: number, quadratureRule: QuadratureRule) {
        this.alpha = alpha;
        this.beta = beta;
        this.gamma = gamma;
        this.quadratureRule = quadratureRule;
    }
}

function lanczos(n: number, quadratureRule: QuadratureRule): [number[], number[], number[], QuadratureRule] {
    if (n <= 0 || n > quadratureRule.x.length) {
        throw new Error('n must be between 1 and len(x).');
    }

    const x = quadratureRule.x;
    const w = quadratureRule.w;
    const alpha = new Array(n).fill(0);
    const beta = n > 1 ? new Array(n - 1).fill(0) : [];
    const gamma = new Array(n).fill(0);

    // Initial polynomial p_0(x) = 1, p_-1(x) = 0 (non-existent, thus ignored in calculations)
    let p0 = new Array(x.length).fill(1);
    let p1 = new Array(x.length).fill(0);

    for (let i = 0; i < n; i++) {
        let pi: number[];

        if (i > 0) {
            pi = (x.map((xi, index) => xi - alpha[i - 1])).map((val, index) => val * p0[index]);
        } else {
            pi = p0;
        }

        if (i > 1) {
            pi = (pi.map((piVal, index) => piVal - beta[i - 1] * p1[index]));
        }

        gamma[i] = dotProduct(w, pi, pi);
        alpha[i] = dotProduct(w, x, pi, pi) / gamma[i];

        if (i < n - 1) {
            beta[i] = dotProduct(w, pi, pi, pi) / gamma[i];
            [p1, p0] = [p0, pi]; // Update polynomials for next iteration
        }
    }

    return [alpha, beta, gamma, quadratureRule];
}
function dotProduct(...arrays: number[][]): number {
    if (arrays.length < 2) {
        throw new Error('At least two arrays are required.');
    }

    if (!arrays.every(arr => arr.length === arrays[0].length)) {
        throw new Error('All arrays must have the same length.');
    }

    return arrays[0].reduce((acc, curr, index) => acc + curr * arrays[1][index], 0);
}
