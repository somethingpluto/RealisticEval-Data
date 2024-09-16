double simpsons_rule(double a, double b, int n) 
{
    double h = (b - a) / n;
    double sum = 0.0;

    for (int idx = 0; idx <= n; idx++) 
    {
        double x = a + idx * h;
        double fx = function_to_integrate(x);

        // See https://en.wikipedia.org/wiki/Simpson's_rule for more information
        //
        // 1) on the first we evaluate f(a) and on the last we evaluate f(b)
        // 2) for steps between we alternate between (4/3)f(a+b) and (2/3)f(a+b)
        // 3) at the end we return h times the weighted sum of all the 1/3, 4/3, 2/3 summation
        //    terms.
        //
        if (idx == 0 || idx == n) 
        {
            sum += fx;
        } 

        // Alternating 4/3 and 2/3 weighting for points between f(a) and f(b)
        else if (idx % 2 == 1) 
        {
            sum += 4.0 * fx;
        } 
        else 
        {
            sum += 2.0 * fx;
        }
    }

    // h=(b-a)/n, sum= [f(a) + f(b)] + (4 or 2)*f(a+b), all multipied by 1/3
    return h * sum / 3.0;
}
