    //secant method for finding bezier t based on x, also provided by ChatGPT
    public static double bezierFindT(double x, double p0, double p1, double p2, double p3) {
        double x0 = 0.4;
        double x1 = 0.6;
        double tolerance = 0.001;
        int iterations = 100;

        for (int i = 0; i < iterations; i++) {
            double fx1 = bezier(x1, p0, p1, p2, p3) - x;
            double fx0 = bezier(x0, p0, p1, p2, p3) - x;
            double xNext = x1 - fx1 * (x1 - x0) / (fx1 - fx0);
            if (Math.abs(xNext - x1) < tolerance)
                return xNext;
            x0 = x1;
            x1 = xNext;
        }

        return x1;
    }