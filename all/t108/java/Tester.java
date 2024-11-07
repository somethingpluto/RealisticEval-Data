package org.real.temp;

import org.junit.Test;

import java.util.Map;

import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testReorderData_ShouldReorderBasedOnScoresInAscendingOrder() {
        int[] imageScores = {90, 85, 95};
        String[] imageNames = {"image1.png", "image2.png", "image3.png"};
        String[] imageIDs = {"id1", "id2", "id3"};

        Map<String, Object> result = reorderData(imageScores, imageNames, imageIDs);

        assertArrayEquals(new int[]{85, 90, 95}, (int[]) result.get("resultScores"));
        assertArrayEquals(new String[]{"image2.png", "image1.png", "image3.png"}, (String[]) result.get("resultNames"));
        assertArrayEquals(new String[]{"id2", "id1", "id3"}, (String[]) result.get("resultIDs"));
    }

    @Test
    public void testReorderData_ShouldReturnSameOrderIfScoresAlreadyAscending() {
        int[] imageScores = {70, 75, 80};
        String[] imageNames = {"imageA.png", "imageB.png", "imageC.png"};
        String[] imageIDs = {"idA", "idB", "idC"};

        Map<String, Object> result = reorderData(imageScores, imageNames, imageIDs);

        assertArrayEquals(new int[]{70, 75, 80}, (int[]) result.get("resultScores"));
        assertArrayEquals(new String[]{"imageA.png", "imageB.png", "imageC.png"}, (String[]) result.get("resultNames"));
        assertArrayEquals(new String[]{"idA", "idB", "idC"}, (String[]) result.get("resultIDs"));
    }

    @Test
    public void testReorderData_ShouldHandleSingleElementArray() {
        int[] imageScores = {50};
        String[] imageNames = {"imageSingle.png"};
        String[] imageIDs = {"idSingle"};

        Map<String, Object> result = reorderData(imageScores, imageNames, imageIDs);

        assertArrayEquals(new int[]{50}, (int[]) result.get("resultScores"));
        assertArrayEquals(new String[]{"imageSingle.png"}, (String[]) result.get("resultNames"));
        assertArrayEquals(new String[]{"idSingle"}, (String[]) result.get("resultIDs"));
    }

    @Test
    public void testReorderData_ShouldHandleEmptyArray() {
        int[] imageScores = {};
        String[] imageNames = {};
        String[] imageIDs = {};

        Map<String, Object> result = reorderData(imageScores, imageNames, imageIDs);

        assertArrayEquals(new int[]{}, (int[]) result.get("resultScores"));
        assertArrayEquals(new String[]{}, (String[]) result.get("resultNames"));
        assertArrayEquals(new String[]{}, (String[]) result.get("resultIDs"));
    }

    @Test
    public void testReorderData_ShouldReorderCorrectlyWithDuplicateScores() {
        int[] imageScores = {88, 88, 92};
        String[] imageNames = {"image1.png", "image2.png", "image3.png"};
        String[] imageIDs = {"id1", "id2", "id3"};

        Map<String, Object> result = reorderData(imageScores, imageNames, imageIDs);

        assertArrayEquals(new int[]{88, 88, 92}, (int[]) result.get("resultScores"));
        assertArrayEquals(new String[]{"image1.png", "image2.png", "image3.png"}, (String[]) result.get("resultNames"));
        assertArrayEquals(new String[]{"id1", "id2", "id3"}, (String[]) result.get("resultIDs"));
    }
}