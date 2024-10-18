package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {

    public static List<List<Integer>> readSequencesFromFile(String filename) {
        List<List<Integer>> sequences = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Assuming sequences are comma-separated in the file
                List<Integer> seq = new ArrayList<>();
                String[] parts = line.strip().split(",");
                for (String part : parts) {
                    seq.add(Integer.parseInt(part));
                }
                sequences.add(seq);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sequences;
    }

    public static boolean isMunodiSequence(List<Integer> sequence) {
        if (sequence.size() < 2) {
            return false;  // A sequence with less than 2 elements cannot be a Munodi sequence
        }

        int commonDifference = sequence.get(1) - sequence.get(0);
        for (int i = 2; i < sequence.size(); i++) {
            if (sequence.get(i) - sequence.get(i - 1) != commonDifference) {
                return false;  // Found a different difference, not a Munodi sequence
            }
        }
        return true;  // All differences are the same
    }

    public static Map<List<Integer>, Boolean> checkSequences(String filename) {
        List<List<Integer>> sequences = readSequencesFromFile(filename);
        Map<List<Integer>, Boolean> results = new HashMap<>();
        for (List<Integer> seq : sequences) {
            results.put(seq, isMunodiSequence(seq));
        }
        return results;
    }

}
