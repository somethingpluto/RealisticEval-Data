#include <iostream>
#include <vector>
#include <stdexcept>
#include <cmath>
#include <numeric>

class QuadratureRule {
public:
    std::vector<double> x;
    std::vector<double> w;
};

class OrthogonalPolynomial {
public:
    std::vector<double> alpha;
    std::vector<double> beta;
    std::vector<double> gamma;
    QuadratureRule quadrature_rule;

    OrthogonalPolynomial(const std::vector<double>& alpha, const std::vector<double>& beta, const std::vector<double>& gamma, const QuadratureRule& quadrature_rule)
        : alpha(alpha), beta(beta), gamma(gamma), quadrature_rule(quadrature_rule) {}
};

std::vector<double> operator*(const std::vector<double>& v1, const std::vector<double>& v2) {
    std::vector<double> result(v1.size());
    for (size_t i = 0; i < v1.size(); ++i) {
        result[i] = v1[i] * v2[i];
    }
    return result;
}

double dotProduct(const std::vector<double>& v1, const std::vector<double>& v2) {
    return std::inner_product(v1.begin(), v1.end(), v2.begin(), 0.0);
}

OrthogonalPolynomial lanczos(int n, const QuadratureRule& quadrature_rule) {
    if (n <= 0 || n > static_cast<int>(quadrature_rule.x.size())) {
        throw std::invalid_argument("n must be between 1 and len(x).");
    }

    const std::vector<double>& x = quadrature_rule.x;
    const std::vector<double>& w = quadrature_rule.w;
    std::vector<double> alpha(n);
    std::vector<double> beta(n - 1, 0.0);
    std::vector<double> gamma(n);

    std::vector<double> p0(x.size(), 1.0);
    std::vector<double> p1(x.size(), 0.0);

    for (int i = 0; i < n; ++i) {
        std::vector<double> pi;
        if (i > 1) {
            pi = (x - std::vector<double>(1, alpha[i - 1])) * p0 - std::vector<double>(1, beta[i - 1]) * p1;
        } else if (i > 0) {
            pi = (x - std::vector<double>(1, alpha[i - 1])) * p0;
        } else {
            pi = p0;
        }

        gamma[i] = dotProduct(w * pi, pi);
        alpha[i] = dotProduct(w * (x * pi), pi) / gamma[i];

        if (i < n - 1) {
            beta[i] = dotProduct(w * pi * pi, pi) / gamma[i];
            p1 = p0;
            p0 = pi;
        }
    }

    return { alpha, beta, gamma, quadrature_rule };
}

// Helper function to subtract a scalar from each element of a vector
std::vector<double> operator-(const std::vector<double>& v, const std::vector<double>& s) {
    std::vector<double> result(v.size());
    for (size_t i = 0; i < v.size(); ++i) {
        result[i] = v[i] - s[0];
    }
    return result;
}