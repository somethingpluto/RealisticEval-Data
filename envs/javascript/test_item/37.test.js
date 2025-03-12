/**
 * Represents a quadrature rule with nodes and weights.
 */
class QuadratureRule {
    /**
     * Constructs a QuadratureRule object.
     * @param {number[]} x - The nodes for the quadrature.
     * @param {number[]} w - The weights for the quadrature.
     */
    constructor(x, w) {
        this.x = x;
        this.w = w;
    }
}

/**
 * Implements the Lanczos function for the recursive relation coefficient algorithm for computing orthogonal polynomials.
 * @param {number} n - The number of orthogonal polynomials to generate.
 * @param {QuadratureRule} quadratureRule - An object containing x (nodes) and w (weights) for the quadrature.
 * @returns {[number[], number[], number[], QuadratureRule]} - The computed coefficients and the quadrature rule.
 */
function lanczos(n, quadratureRule) {
    const { x, w } = quadratureRule;
    const alpha = new Array(n).fill(0);
    const beta = new Array(n).fill(0);
    const gamma = new Array(n).fill(0);

    // Initialize the first polynomial
    let p0 = new Array(x.length).fill(1);
    let p1 = x.map((xi) => xi);

    // Compute the coefficients
    for (let k = 0; k < n; k++) {
        alpha[k] = dotProduct(p1, p1, w) / dotProduct(p1, p0, w);
        beta[k] = dotProduct(p1, p1, w) / dotProduct(p0, p0, w);
        gamma[k] = dotProduct(p1, p1, w) / dotProduct(p1, p1, w);

        if (k < n - 1) {
            const pNext = x.map((xi, i) => (xi - alpha[k]) * p1[i] - beta[k] * p0[i]);
            p0 = p1;
            p1 = pNext;
        }
    }

    return [alpha, beta, gamma, quadratureRule];
}

/**
 * Computes the dot product of two vectors with respect to the weights.
 * @param {number[]} u - The first vector.
 * @param {number[]} v - The second vector.
 * @param {number[]} w - The weights.
 * @returns {number} - The dot product.
 */
function dotProduct(u, v, w) {
    return u.reduce((sum, ui, i) => sum + ui * v[i] * w[i], 0);
}
class QuadratureRule {
    constructor(x, w) {
        this.x = x;
        this.w = w;
    }
}

describe('OrthogonalPolynomial Tests', () => {
    test('lanczos basic', () => {
        const x = [0.0, 0.5, 1.0];
        const w = [0.333, 0.333, 0.334];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 2;
        const { alpha, beta, gamma } = lanczos(n, quadratureRule);

        expect(alpha.length).toBe(n);
        expect(beta.length).toBe(n - 1);
        expect(gamma.length).toBe(n);
    });

    test('lanczos n greater than length', () => {
        const x = [0.0, 0.5, 1.0];
        const w = [0.333, 0.333, 0.334];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 4;

        expect(() => lanczos(n, quadratureRule)).toThrow('n must be between 1 and len(x).');
    });

    test('lanczos n zero', () => {
        const x = [0.0, 0.5, 1.0];
        const w = [0.333, 0.333, 0.334];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 0;

        expect(() => lanczos(n, quadratureRule)).toThrow('n must be between 1 and len(x).');
    });

    test('lanczos weights nonuniform', () => {
        const x = [0.0, 0.5, 1.0];
        const w = [0.1, 0.4, 0.5];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 3;
        const { alpha, beta, gamma } = lanczos(n, quadratureRule);

        expect(alpha.length).toBe(n);
        expect(beta.length).toBe(n - 1);
        expect(gamma.length).toBe(n);
        expect(gamma.every(g => g > 0)).toBe(true);
    });

    test('lanczos single node', () => {
        const x = [0.5];
        const w = [1.0];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 1;
        const { alpha, beta, gamma } = lanczos(n, quadratureRule);

        expect(alpha.length).toBe(n);
        expect(beta.length).toBe(n - 1);
        expect(gamma.length).toBe(n);
        expect(gamma.every(g => g > 0)).toBe(true);
    });
});
