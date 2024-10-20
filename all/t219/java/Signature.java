/**
 * Check for ticker symbols with the same ex-dividend date but different dividend amounts.
 * 
 * @param records A list of tuples where each tuple contains (ticker, exDividendDate, dividendAmount).
 * @return A list of tuples where each tuple contains (ticker, exDividendDate) that have different dividend amounts.
 */
public static class Tuple<T1, T2> {
    private T1 first;
    private T2 second;

    public Tuple(T1 first, T2 second) {
        this.first = first;
        this.second = second;
    }

    public T1 getFirst() {
        return first;
    }

    public T2 getSecond() {
        return second;
    }
}
public static List<Tuple<String, String>> checkDividendVariances(List<Tuple<String, String, Integer>> records) {}