package org.real.temp;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {
    public static Map<String, Object> reorderData(int[] imageScores, String[] imageNames, String[] imageIDs) {
        List<ImageData> imageDataList = new ArrayList<>();

        for (int i = 0; i < imageScores.length; i++) {
            imageDataList.add(new ImageData(imageScores[i], imageNames[i], imageIDs[i]));
        }

        imageDataList.sort(Comparator.comparingInt(data -> data.score));

        int[] resultScores = imageDataList.stream().mapToInt(data -> data.score).toArray();
        String[] resultNames = imageDataList.stream().map(data -> data.name).toArray(String[]::new);
        String[] resultIDs = imageDataList.stream().map(data -> data.id).toArray(String[]::new);

        Map<String, Object> result = new HashMap<>();
        result.put("resultScores", resultScores);
        result.put("resultNames", resultNames);
        result.put("resultIDs", resultIDs);
        
        return result;
    }

    private static class ImageData {
        int score;
        String name;
        String id;

        ImageData(int score, String name, String id) {
            this.score = score;
            this.name = name;
            this.id = id;
        }
    }
}