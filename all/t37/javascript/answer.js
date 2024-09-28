class OrthogonalPolynomial {
    constructor(alpha, beta, gamma, quadratureRule) {
        this.alpha = alpha;
        this.beta = beta;
        this.gamma = gamma;
        this.quadratureRule = quadratureRule;
    }
}

function dotProduct(a, b) {
    return a.reduce((sum, ai, i) => sum + ai * b[i], 0);
}

function lanczos(n, quadratureRule) {
    if (n <= 0 || n > quadratureRule.x.length) {
        throw new Error('n must be between 1 and len(x).');
    }

    let x = quadratureRule.x;
    let w = quadratureRule.w;
    
    let alpha = new Array(n).fill(0);
    let beta = n > 1 ? new Array(n - 1).fill(0) : [];
    let gamma = new Array(n).fill(0);

    let p0 = new Array(x.length).fill(1);  // Initial polynomial p_0(x) = 1
    let p1 = new Array(x.length).fill(0);  // p_-1(x) = 0 (non-existent, thus ignored in calculations)

    for (let i = 0; i < n; i++) {
        let pi;
        if (i > 0) {
            pi = x.map((xi, j) => (xi - alpha[i - 1]) * p0[j]);
        } else {
            pi = [...p0];
        }

        gamma[i] = dotProduct(w.map((wi, j) => wi * pi[j] * pi[j]), pi);
        alpha[i] = dotProduct(w.map((wi, j) => wi * x[j] * pi[j]), pi) / gamma[i];

        if (i < n - 1) {
            beta[i] = dotProduct(w.map((wi, j) => wi * pi[j] * pi[j]), pi) / gamma[i];
            // Update polynomials for next iteration
            [p1, p0] = [p0, pi];
        }
    }

    return { alpha, beta, gamma, quadratureRule };
}