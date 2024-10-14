package org.real.temp;

import org.junit.Test;
import java.util.Arrays;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testExtractsCategoriesAndCleansTheSummaryCorrectly() {
        String input = "This is a summary. Categories: [Technology, Health]";
        CategoryParser.Result expected = new CategoryParser.Result("This is a summary.", Arrays.asList("Technology", "Health"));
        assertEquals(expected.summary, CategoryParser.parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, CategoryParser.parseCategoriesFromSummary(input).categories);
    }

    @Test
    public void testReturnsEmptyCategoriesAndOriginalSummaryWhenNoCategoriesArePresent() {
        String input = "This is a summary without categories.";
        CategoryParser.Result expected = new CategoryParser.Result("This is a summary without categories.", Arrays.asList());
        assertEquals(expected.summary, CategoryParser.parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, CategoryParser.parseCategoriesFromSummary(input).categories);
    }

    @Test
    public void testIgnoresCaseOfTheCategoryPrefix() {
        String input = "Summary text. categories: [Education, Science]";
        CategoryParser.Result expected = new CategoryParser.Result("Summary text.", Arrays.asList("Education", "Science"));
        assertEquals(expected.summary, CategoryParser.parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, CategoryParser.parseCategoriesFromSummary(input).categories);
    }

    @Test
    public void testHandlesExtraSpacesAndMalformedCategoryStringsCorrectly() {
        String input = "Details follow. Categories: [ Business ,  , Finance]";
        CategoryParser.Result expected = new CategoryParser.Result("Details follow.", Arrays.asList("Business", "Finance"));
        assertEquals(expected.summary, CategoryParser.parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, CategoryParser.parseCategoriesFromSummary(input).categories);
    }

    @Test
    public void testRemovesTheCategoryStringCorrectlyEvenIfItAppearsInTheMiddleOfTheSummary() {
        String input = "Beginning of summary. Categories: [Art, Design] Continuation of summary.";
        CategoryParser.Result expected = new CategoryParser.Result("Beginning of summary. Continuation of summary.", Arrays.asList("Art", "Design"));
        assertEquals(expected.summary, CategoryParser.parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, CategoryParser.parseCategoriesFromSummary(input).categories);
    }
}