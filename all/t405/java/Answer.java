package org.real.temp;

public class Answer {
    
    /**
     * Removes the part before the first uppercase letter and the first lowercase letter from the string.
     *
     * @param strings Accepts one or more strings as variable arguments.
     */
    public static void removePartsOfString(String... strings) {
        for (String str : strings) {
            if (str == null || str.isEmpty()) {
                System.out.println("Input string is null or empty");
                continue;
            }

            int startIndex = -1;
            boolean foundUppercase = false;
            boolean foundLowercase = false;

            // Find the index of the first uppercase and lowercase character
            for (int i = 0; i < str.length(); i++) {
                char ch = str.charAt(i);
                if (!foundUppercase && Character.isUpperCase(ch)) {
                    foundUppercase = true;
                    startIndex = i;
                }
                if (!foundLowercase && Character.isLowerCase(ch)) {
                    foundLowercase = true;
                    startIndex = i;
                }
                if (foundUppercase && foundLowercase) {
                    break;
                }
            }

            // If both uppercase and lowercase characters are found, print the substring starting from the first found character
            if (startIndex != -1) {
                String result = str.substring(startIndex);
                System.out.println(result);
            } else {
                System.out.println("No uppercase or lowercase character found");
            }
        }
    }

    public static void main(String[] args) {
        removePartsOfString("1234AbCde5678", "HelloWorld", "JavaProgramming");
    }
}