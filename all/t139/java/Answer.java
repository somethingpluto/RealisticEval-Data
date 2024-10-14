package org.real.temp;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {
    /**
     * Extracts categories from a summarized output string and returns the cleaned summary and categories.
     *
     * @param summarizedOutput The summary text potentially containing categorized question.
     * @return An object containing the cleaned summary text and an array of categories.
     */
    public static Result parseCategoriesFromSummary(String summarizedOutput) {
        // Define the regex to find the categories pattern in the summary
        String categoriesRegex = "Categories:\\s*\\[([^]]+)\\]";
        Pattern pattern = Pattern.compile(categoriesRegex, Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(summarizedOutput);

        List<String> categories = new ArrayList<>();
        String summary = summarizedOutput;

        // If a match is found, process the categories and clean the summary
        if (matcher.find()) {
            String categoriesString = matcher.group(1);
            for (String category : categoriesString.split(",")) {
                String trimmedCategory = category.trim();
                if (!trimmedCategory.isEmpty()) {
                    categories.add(trimmedCategory);
                }
            }

            // Remove the category line from the summary and trim any leading/trailing whitespace
            summary = summarizedOutput.replace(matcher.group(0), "").trim();
        }

        return new Result(summary, categories);
    }

    public static class Result {
        public final String summary;
        public final List<String> categories;

        public Result(String summary, List<String> categories) {
            this.summary = summary;
            this.categories = categories;
        }
    }
}