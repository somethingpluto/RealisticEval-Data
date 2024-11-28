package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Extracts the title, author, and year from a BibTeX file.
     *
     * @param bibFile The path to the BibTeX file.
     * @return A list containing dictionaries with title, author, and year for each article.
     */
    public static List<Dictionary> extractBibInfo(String bibFile) {
        List<Dictionary> articles = new ArrayList<>();

        // Regular expressions to match title, author, and year
        Pattern titlePattern = Pattern.compile("title\\s*=\\s*{([^}]*)}", Pattern.CASE_INSENSITIVE);
        Pattern authorPattern = Pattern.compile("author\\s*=\\s*{([^}]*)}", Pattern.CASE_INSENSITIVE);
        Pattern yearPattern = Pattern.compile("year\\s*=\\s*{([^}]*)}", Pattern.CASE_INSENSITIVE);

        try (BufferedReader reader = new BufferedReader(new FileReader(bibFile))) {
            StringBuilder content = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }

            // Split the content into individual entries based on '@'
            String[] entries = content.toString().split("@");

            // Skip the first split, which is empty
            for (int i = 1; i < entries.length; i++) {
                Matcher titleMatcher = titlePattern.matcher(entries[i]);
                Matcher authorMatcher = authorPattern.matcher(entries[i]);
                Matcher yearMatcher = yearPattern.matcher(entries[i]);

                Dictionary article = new Dictionary();

                if (titleMatcher.find()) {
                    article.put("title", titleMatcher.group(1));
                } else {
                    article.put("title", null);
                }

                if (authorMatcher.find()) {
                    article.put("author", authorMatcher.group(1));
                } else {
                    article.put("author", null);
                }

                if (yearMatcher.find()) {
                    article.put("year", yearMatcher.group(1));
                } else {
                    article.put("year", null);
                }

                articles.add(article);
            }

        } catch (IOException e) {
            System.out.println("Error: The file '" + bibFile + "' was not found.");
        }

        return articles;
    }

    public static void main(String[] args) {
        List<Dictionary> articles = extractBibInfo("path/to/bibtex/file.bib");
        for (Dictionary article : articles) {
            System.out.println(article);
        }
    }

    // Simple implementation of a dictionary (key-value store)
    public static class Dictionary {
        private final java.util.Map<String, String> map = new java.util.HashMap<>();

        public void put(String key, String value) {
            map.put(key, value);
        }

        @Override
        public String toString() {
            return map.toString();
        }
    }
}