package org.real.temp;

public class Answer {
    public static String fixIndentation(String code) {
        String[] lines = code.split("\n");
        StringBuilder fixedCode = new StringBuilder();
        int currentIndentLevel = 0;
        int spacesPerIndent = 4;

        for (String line : lines) {
            String trimmedLine = line.trim();

            if (trimmedLine.isEmpty()) {
                fixedCode.append("\n");
                continue;
            }

            // Adjust current indentation level
            if (trimmedLine.startsWith("elif") || trimmedLine.startsWith("else") || trimmedLine.startsWith("except") || trimmedLine.startsWith("finally")) {
                currentIndentLevel -= 1;
            } else if (trimmedLine.startsWith("return") || trimmedLine.startsWith("break") || trimmedLine.startsWith("continue") || trimmedLine.startsWith("pass")) {
                currentIndentLevel -= 1;
            }

            // Add appropriate indentation
            for (int i = 0; i < currentIndentLevel * spacesPerIndent; i++) {
                fixedCode.append(" ");
            }
            fixedCode.append(trimmedLine).append("\n");

            // Increase indent level after lines ending with a colon
            if (trimmedLine.endsWith(":")) {
                currentIndentLevel += 1;
            } else if (trimmedLine.startsWith("return") || trimmedLine.startsWith("break") || trimmedLine.startsWith("continue") || trimmedLine.startsWith("pass")) {
                currentIndentLevel -= 1;
            }
        }

        return fixedCode.toString();
    }
}
