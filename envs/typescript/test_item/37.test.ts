// ... (previous code for context)

/**
 * Computes the next alpha coefficient using the Lanczos algorithm.
 * @param {number} n The current index.
 * @param {number} alpha The current alpha coefficient.
 * @param {number} beta The current beta coefficient.
 * @param {number} gamma The current gamma coefficient.
 * @param {number[]} x The nodes of the quadrature rule.
 * @param {number[]} w The weights of the quadrature rule.
 * @returns The next alpha coefficient.
 */
function computeAlpha(n: number, alpha: number, beta: number, gamma: number, x: number[], w: number[]): number {
    // Implementation of alpha computation
}

/**
 * Computes the next beta coefficient using the Lanczos algorithm.
 * @param {number} n The current index.
 * @param {number} alpha The current alpha coefficient.
 * @param {number} beta The current beta coefficient.
 * @param {number} gamma The current gamma coefficient.
 * @param {number[]} x The nodes of the quadrature rule.
 * @param {number[]} w The weights of the quadrature rule.
 * @returns The next beta coefficient.
 */
function computeBeta(n: number, alpha: number, beta: number, gamma: number, x: number[], w: number[]): number {
    // Implementation of beta computation
}

// ... (rest of the lanczos function and other code)
class QuadratureRule {
    x: number[];
    w: number[];

    constructor(x: number[], w: number[]) {
        this.x = x;
        this.w = w;
    }
}
describe('OrthogonalPolynomial', () => {

    test('test_lanczos_basic', () => {
        const x = [0.0, 0.5, 1.0];
        const w = [0.333, 0.333, 0.334];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 2;
        const [alpha, beta, gamma] = lanczos(n, quadratureRule);

        expect(alpha.length).toBe(n);
        expect(beta.length).toBe(n - 1);
        expect(gamma.length).toBe(n);
    });

    test('test_lanczos_n_greater_than_length', () => {
        const x = [0.0, 0.5, 1.0];
        const w = [0.333, 0.333, 0.334];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 4;

        expect(() => lanczos(n, quadratureRule)).toThrowError('n must be between 1 and len(x).');
    });

    test('test_lanczos_n_zero', () => {
        const x = [0.0, 0.5, 1.0];
        const w = [0.333, 0.333, 0.334];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 0;

        expect(() => lanczos(n, quadratureRule)).toThrowError('n must be between 1 and len(x).');
    });

    test('test_lanczos_weights_nonuniform', () => {
        const x = [0.0, 0.5, 1.0];
        const w = [0.1, 0.4, 0.5];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 3;
        const [alpha, beta, gamma] = lanczos(n, quadratureRule);

        expect(alpha.length).toBe(n);
        expect(beta.length).toBe(n - 1);
        expect(gamma.length).toBe(n);
        expect(gamma.every(value => value > 0)).toBe(true);
    });

    test('test_lanczos_single_node', () => {
        const x = [0.5];
        const w = [1.0];
        const quadratureRule = new QuadratureRule(x, w);
        const n = 1;
        const [alpha, beta, gamma] = lanczos(n, quadratureRule);

        expect(alpha.length).toBe(n);
        expect(beta.length).toBe(n - 1);
        expect(gamma.length).toBe(n);
        expect(gamma.every(value => value > 0)).toBe(true);
    });

});
