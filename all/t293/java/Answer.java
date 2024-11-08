package org.real.temp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;



public class Answer {

    static class ImageData {
        double score;
        String name;
        String id;

        ImageData(double score, String name, String id) {
            this.score = score;
            this.name = name;
            this.id = id;
        }
    }

    public static Result reorderData(double[] imageScores, String[] imageNames, String[] imageIDs) {
        // Combine scores, names, and IDs into a list of ImageData objects
        List<ImageData> imageDataList = new ArrayList<>();
        for (int i = 0; i < imageScores.length; i++) {
            imageDataList.add(new ImageData(imageScores[i], imageNames[i], imageIDs[i]));
        }

        // Sort imageDataList by scores in ascending order
        imageDataList.sort(Comparator.comparingDouble(data -> data.score));

        // Prepare the result arrays
        double[] resultScores = new double[imageDataList.size()];
        String[] resultNames = new String[imageDataList.size()];
        String[] resultIDs = new String[imageDataList.size()];

        for (int i = 0; i < imageDataList.size(); i++) {
            ImageData data = imageDataList.get(i);
            resultScores[i] = data.score;
            resultNames[i] = data.name;
            resultIDs[i] = data.id;
        }

        return new Result(resultScores, resultNames, resultIDs);
    }

    // Result class to hold the output
    public static class Result {
        public double[] resultScores;
        public String[] resultNames;
        public String[] resultIDs;

        public Result(double[] resultScores, String[] resultNames, String[] resultIDs) {
            this.resultScores = resultScores;
            this.resultNames = resultNames;
            this.resultIDs = resultIDs;
        }
    }

    public static void main(String[] args) {
        // Example usage
        double[] scores = {3.5, 2.0, 4.1};
        String[] names = {"Image1", "Image2", "Image3"};
        String[] ids = {"ID1", "ID2", "ID3"};

        Result result = reorderData(scores, names, ids);

        System.out.println(Arrays.toString(result.resultScores));
        System.out.println(Arrays.toString(result.resultNames));
        System.out.println(Arrays.toString(result.resultIDs));
    }
}