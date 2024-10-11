package org.real.temp;

import java.util.List;
import java.util.stream.Collectors;

public class Answer {
    /**
     * Sums up calibration values extracted from the document.
     * Each calibration value is formed by combining the first and last digits of numbers found in each line
     * into a two-digit number.
     *
     * @param calibrationDocument An iterable of strings, each representing a line of text.
     * @return The total sum of all calibration values.
     */
    public static int sumCalibrationValues(List<String> calibrationDocument) {
        return calibrationDocument.stream()
                .flatMapToInt(Answer::extractCalibrationValue)
                .sum();
    }

    private static IntStream extractCalibrationValue(String line) {
        return Pattern.compile("\\d+")
                .matcher(line)
                .results()
                .map(matchResult -> {
                    String number = matchResult.group();
                    if (number.length() == 1) {
                        return Integer.parseInt(number + "0");
                    } else {
                        return Integer.parseInt("" + number.charAt(0) + number.charAt(number.length() - 1));
                    }
                })
                .boxed()
                .mapToInt(Integer::intValue);
    }
}