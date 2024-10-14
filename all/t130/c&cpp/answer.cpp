#include <iostream>
#include <mpfr.h>

void computePi(int digits) {
    // Set the precision for mpfr calculations
    mpfr_set_default_prec(digits * 3.321928); // log2(10) for decimal to binary conversion

    mpfr_t a, b, t, p, a_next, b_next, t_next, p_next, pi, prev_pi;
    mpfr_init2(a, digits);
    mpfr_init2(b, digits);
    mpfr_init2(t, digits);
    mpfr_init2(p, digits);
    mpfr_init2(a_next, digits);
    mpfr_init2(b_next, digits);
    mpfr_init2(t_next, digits);
    mpfr_init2(p_next, digits);
    mpfr_init2(pi, digits);
    mpfr_init2(prev_pi, digits);

    mpfr_set_d(a, 1.0, MPFR_RNDN);
    mpfr_sqrt(b, mpfr_set_d(b, 0.5), MPFR_RNDN); // b0 = 1/sqrt(2)
    mpfr_set_d(t, 0.25, MPFR_RNDN);               // t0 = 1/4
    mpfr_set_d(p, 1.0, MPFR_RNDN);

    // Iterate until the desired precision is reached
    for (int i = 0; i < 10; ++i) {
        mpfr_add(a_next, a, b, MPFR_RNDN);
        mpfr_div_ui(a_next, a_next, 2, MPFR_RNDN); // aNext = (a + b) / 2
        mpfr_mul(b_next, a, b, MPFR_RNDN);
        mpfr_sqrt(b_next, b_next, MPFR_RNDN);     // bNext = sqrt(a * b)

        mpfr_sub(a, a, a_next, MPFR_RNDN);
        mpfr_pow_ui(a, a, 2, MPFR_RNDN);           // diff^2
        mpfr_mul(t_next, p, a, MPFR_RNDN);
        mpfr_sub(t, t, t_next, MPFR_RNDN);         // tNext = t - p * diff^2
        mpfr_mul_ui(p_next, p, 2, MPFR_RNDN);      // pNext = 2 * p

        mpfr_set(a, a_next, MPFR_RNDN);
        mpfr_set(b, b_next, MPFR_RNDN);
        mpfr_set(t, t_next, MPFR_RNDN);
        mpfr_set(p, p_next, MPFR_RNDN);

        mpfr_add(pi, a, b, MPFR_RNDN);
        mpfr_pow_ui(pi, pi, 2, MPFR_RNDN);
        mpfr_mul_ui(t, t, 4, MPFR_RNDN);
        mpfr_div(pi, pi, t, MPFR_RNDN);

        // Check if the desired precision has been reached
        if (mpfr_cmp(pi, prev_pi) == 0) {
            break;
        }
        mpfr_set(prev_pi, pi, MPFR_RNDN);
    }

    // Print π to the specified number of digits
    mpfr_exp(pi, pi, MPFR_RNDN); // Convert to string format
    mpfr_printf("%.10Ff\n", pi); // Print to specified precision

    // Clear memory
    mpfr_clear(a);
    mpfr_clear(b);
    mpfr_clear(t);
    mpfr_clear(p);
    mpfr_clear(a_next);
    mpfr_clear(b_next);
    mpfr_clear(t_next);
    mpfr_clear(p_next);
    mpfr_clear(pi);
    mpfr_clear(prev_pi);
}