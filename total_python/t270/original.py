import scipy.special as sp
import scipy.stats as stats
from scipy.integrate import quad


def beta_dist_max_prob(alpha, beta, i):
    """
    Given a list of alpha and beta parameters for a set of beta distributions,
    and an index i, return the probability that a sample from the i-th distribution
    will be the maximum among all samples from all distributions.

    Written by ChatGPT.
    """

    def integrand(x_i):
        product_term = 1
        for j in range(len(alpha)):
            if j != i:
                product_term *= sp.betainc(alpha[j], beta[j], x_i)
        return product_term * stats.beta.pdf(x_i, alpha[i], beta[i])

    result, _ = quad(integrand, 0, 1, limit=10_000)
    return result