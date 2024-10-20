/**
 * Extracts categories from a summarized output string and returns the cleaned summary and categories.
 * The categories are expected to be in the format "Categories: [category1, category2, ...]".
 *
 * @param summarizedOutput The summary text potentially containing categorized question.
 * @return A Result object containing the cleaned summary text and a list of categories.
 */
public static class Result {
    public final String summary;
    public final List<String> categories;

    public Result(String summary, List<String> categories) {
        this.summary = summary;
        this.categories = categories;
    }
}
public static Result parseCategoriesFromSummary(String summarizedOutput) {}