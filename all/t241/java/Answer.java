import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Answer {

    public static Pair<Integer, Integer> getMinSeqNumAndDistance(String filePath, String word1, String word2) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            int minLineNumber = -1;
            int minDistance = Integer.MAX_VALUE;

            int lineNumber = 0;
            while ((line = br.readLine()) != null) {
                lineNumber++;
                String[] words = line.split("\\s+");
                boolean word1Found = false;
                boolean word2Found = false;

                for (int i = 0; i < words.length; i++) {
                    if (words[i].equals(word1)) {
                        word1Found = true;
                        if (word2Found) {
                            int distance = Math.abs(i - word2Index);
                            if (distance < minDistance) {
                                minDistance = distance;
                                minLineNumber = lineNumber;
                            }
                        }
                    } else if (words[i].equals(word2)) {
                        word2Found = true;
                        if (word1Found) {
                            int distance = Math.abs(i - word1Index);
                            if (distance < minDistance) {
                                minDistance = distance;
                                minLineNumber = lineNumber;
                            }
                        }
                    }

                    if (word1Found && word2Found) {
                        break;
                    }
                }
            }

            return new Pair<>(minLineNumber, minDistance == Integer.MAX_VALUE ? null : minDistance);

        } catch (IOException e) {
            e.printStackTrace();
            return new Pair<>(null, null);
        }
    }
}

class Pair<T, U> {
    private T first;
    private U second;

    public Pair(T first, U second) {
        this.first = first;
        this.second = second;
    }

    public T getFirst() {
        return first;
    }

    public U getSecond() {
        return second;
    }
}