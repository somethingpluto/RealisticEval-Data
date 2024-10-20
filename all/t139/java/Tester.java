package org.real.temp;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testExtractsCategoriesAndCleansTheSummaryCorrectly() {
        String input = "This is a summary. Categories: [Technology, Health]";
        Result expected = new Result("This is a summary.", Arrays.asList("Technology", "Health"));
        assertEquals(expected.summary, parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, parseCategoriesFromSummary(input).categories);
    }

    @Test
    public void testReturnsEmptyCategoriesAndOriginalSummaryWhenNoCategoriesArePresent() {
        String input = "This is a summary without categories.";
        Result expected = new Result("This is a summary without categories.", Arrays.asList());
        assertEquals(expected.summary, parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, parseCategoriesFromSummary(input).categories);
    }

    @Test
    public void testIgnoresCaseOfTheCategoryPrefix() {
        String input = "Summary text. categories: [Education, Science]";
        Result expected = new Result("Summary text.", Arrays.asList("Education", "Science"));
        assertEquals(expected.summary, parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, parseCategoriesFromSummary(input).categories);
    }

    @Test
    public void testHandlesExtraSpacesAndMalformedCategoryStringsCorrectly() {
        String input = "Details follow. Categories: [ Business ,  , Finance]";
        Result expected = new Result("Details follow.", Arrays.asList("Business", "Finance"));
        assertEquals(expected.summary, parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, parseCategoriesFromSummary(input).categories);
    }

    @Test
    public void testRemovesTheCategoryStringCorrectlyEvenIfItAppearsInTheMiddleOfTheSummary() {
        String input = "Beginning of summary. Categories: [Art, Design] Continuation of summary.";
        Result expected = new Result("Beginning of summary. Continuation of summary.", Arrays.asList("Art", "Design"));
        assertEquals(expected.summary, parseCategoriesFromSummary(input).summary);
        assertEquals(expected.categories, parseCategoriesFromSummary(input).categories);
    }
}