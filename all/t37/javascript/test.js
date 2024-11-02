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
        expect(gamma.every(g => g > 0)).toBe(false);
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