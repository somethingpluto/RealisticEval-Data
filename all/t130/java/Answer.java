import java.math.BigDecimal;
import java.math.MathContext;

public class PiCalculator {
    public static String computePi(int digits) {
        MathContext mc = new MathContext(digits + 10); // Extra precision
        BigDecimal one = BigDecimal.ONE;
        BigDecimal two = new BigDecimal("2");
        BigDecimal four = new BigDecimal("4");
        BigDecimal half = new BigDecimal("0.5");

        // Initialize variables
        BigDecimal a = one;
        BigDecimal b = one.divide(two).sqrt(mc); // b0 = 1 / sqrt(2)
        BigDecimal t = one.divide(four, mc);     // t0 = 1/4
        BigDecimal p = one;

        BigDecimal prevPi = BigDecimal.ZERO;
        BigDecimal pi;

        // Iterate until the desired precision is reached
        for (int i = 0; i < 10; i++) {
            BigDecimal aNext = a.add(b).divide(two, mc);
            BigDecimal bNext = a.multiply(b).sqrt(mc);
            BigDecimal diff = a.subtract(aNext);
            BigDecimal tNext = t.subtract(p.multiply(diff.pow(2, mc), mc), mc);
            BigDecimal pNext = p.multiply(two, mc);

            a = aNext;
            b = bNext;
            t = tNext;
            p = pNext;

            pi = a.add(b).pow(2, mc).divide(t.multiply(four, mc), mc);

            // Check if the desired precision has been reached
            if (pi.compareTo(prevPi) == 0) {
                break;
            }
            prevPi = pi;
        }

        // Return π to the specified number of digits
        return pi.setScale(digits, BigDecimal.ROUND_DOWN).toString();
    }
}