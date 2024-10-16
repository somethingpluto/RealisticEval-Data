package org.real.temp;
public class Answer {

    public static boolean isCamelCase(String input) {
        // Regular expression to match CAMEL_CASE
        String camelCaseRegex = "^[a-z]+([A-Z][a-z]*)*$";
        return input.matches(camelCaseRegex);
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(isCamelCase("camelCase")); // true
        System.out.println(isCamelCase("CamelCase")); // false
        System.out.println(isCamelCase("camelcase")); // true
        System.out.println(isCamelCase("camelCaseExample")); // true
    }
}