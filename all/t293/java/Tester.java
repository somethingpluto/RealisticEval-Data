package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSortsQuestionCorrectlyForBasicInputs() {
        double[] scores = {3, 1, 2};
        String[] names = {"Image3", "Image1", "Image2"};
        String[] ids = {"103", "101", "102"};

        Result expected = new Result(
            new double[]{1, 2, 3},
            new String[]{"Image1", "Image2", "Image3"},
            new String[]{"101", "102", "103"}
        );

        assertArrayEquals(expected.resultScores, reorderData(scores, names, ids).resultScores, 0.001);
        assertArrayEquals(expected.resultNames, reorderData(scores, names, ids).resultNames);
        assertArrayEquals(expected.resultIDs, reorderData(scores, names, ids).resultIDs);
    }

    @Test
    public void testSortsQuestionCorrectlyWithMixedScores() {
        double[] scores = {5, 1, 3, 5, 2};
        String[] names = {"Image5", "Image1", "Image3", "Image6", "Image2"};
        String[] ids = {"105", "101", "103", "106", "102"};

        Result expected = new Result(
            new double[]{1, 2, 3, 5, 5},
            new String[]{"Image1", "Image2", "Image3", "Image5", "Image6"},
            new String[]{"101", "102", "103", "105", "106"}
        );

        assertArrayEquals(expected.resultScores, reorderData(scores, names, ids).resultScores, 0.001);
        assertArrayEquals(expected.resultNames, reorderData(scores, names, ids).resultNames);
        assertArrayEquals(expected.resultIDs, reorderData(scores, names, ids).resultIDs);
    }

    @Test
    public void testHandlesDuplicateScores() {
        double[] scores = {2, 2, 1};
        String[] names = {"Image2", "Image3", "Image1"};
        String[] ids = {"102", "103", "101"};

        Result expected = new Result(
            new double[]{1, 2, 2},
            new String[]{"Image1", "Image2", "Image3"},
            new String[]{"101", "102", "103"}
        );

        assertArrayEquals(expected.resultScores, reorderData(scores, names, ids).resultScores, 0.001);
        assertArrayEquals(expected.resultNames, reorderData(scores, names, ids).resultNames);
        assertArrayEquals(expected.resultIDs, reorderData(scores, names, ids).resultIDs);
    }

    @Test
    public void testHandlesEmptyArrays() {
        double[] scores = {};
        String[] names = {};
        String[] ids = {};

        Result expected = new Result(
            new double[]{},
            new String[]{},
            new String[]{}
        );

        assertArrayEquals(expected.resultScores, reorderData(scores, names, ids).resultScores, 0.001);
        assertArrayEquals(expected.resultNames, reorderData(scores, names, ids).resultNames);
        assertArrayEquals(expected.resultIDs, reorderData(scores, names, ids).resultIDs);
    }
}