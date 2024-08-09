double trapezoidal_rule(double a, double b, int n) 
{
    double h = (b - a) / n;
    double sum = (function_to_integrate(a) + function_to_integrate(b)) / 2.0;

    for (int i = 1; i < n; i++) 
    {
        double x = a + i * h;
        sum += function_to_integrate(x);
    }

    return h * sum;
}
