package org.real.temp;

import java.util.*;
import java.util.regex.*;

public class Answer {

    /**
     * This method modifies a SQL query string containing named parameters
     * (like $name, $age) into a format compatible with libraries that require
     * positional parameters (like $1, $2, etc.), such as asyncpg. It returns
     * a tuple containing the modified SQL string and a list of parameter values
     * ordered according to their new positions in the query.
     *
     * @param sql The original SQL query string with named parameters.
     * @param params A map mapping parameter names to their values.
     * @return A Pair where the first element is the modified SQL query string
     *         with positional parameters, and the second element is a list of
     *         parameter values sorted according to the order of the positional parameters.
     */
    public static Pair<String, List<Object>> prepareQuery(String sql, Map<String, Object> params) {
        // Find all occurrences of named parameters in the SQL string
        Pattern pattern = Pattern.compile("\\$\\w+");
        Matcher matcher = pattern.matcher(sql);
        Set<String> namedParams = new LinkedHashSet<>();

        while (matcher.find()) {
            namedParams.add(matcher.group());
        }

        // Convert the set back to a list to maintain the order
        List<String> uniqueParams = new ArrayList<>(namedParams);

        // Substitute each named parameter with its corresponding positional parameter
        for (int index = 0; index < uniqueParams.size(); index++) {
            String param = uniqueParams.get(index);
            String replacement = "$" + (index + 1);
            sql = sql.replace(param, replacement);
        }

        // Prepare the list of values corresponding to the order of the positional parameters
        List<Object> values = new ArrayList<>();
        for (String param : uniqueParams) {
            if (params.containsKey(param.substring(1))) { // Remove the '$' prefix
                values.add(params.get(param.substring(1)));
            }
        }

        return new Pair<>(sql, values);
    }

    // A simple implementation of a Pair class since Java does not have a built-in Pair class
    public static class Pair<T, U> {
        private final T first;
        private final U second;

        public Pair(T first, U second) {
            this.first = first;
            this.second = second;
        }

        public T getFirst() {
            return first;
        }

        public U getSecond() {
            return second;
        }
    }

    // Example usage
    public static void main(String[] args) {
        String sql = "SELECT * FROM users WHERE $name = 'John' AND $age > 30";
        Map<String, Object> params = new HashMap<>();
        params.put("name", "John");
        params.put("age", 30);

        Pair<String, List<Object>> result = prepareQuery(sql, params);
        System.out.println("Modified SQL: " + result.getFirst());
        System.out.println("Values: " + result.getSecond());
    }
}