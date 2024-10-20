package org.real.temp;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Split the input text string into sentences.
     *
     * @param text The input text to be split into sentences.
     * @return A list of sentences extracted from the input text, cleaned and stripped of leading/trailing whitespace.
     */
    public static List<String> splitIntoSentences(String text) {
        // Check if the input is a string
        if (text == null) {
            throw new IllegalArgumentException("Input must be a string.");
        }

        // Regular expression to split the text where there is a punctuation followed by space or end of string
        // This handles situations where punctuation might be followed by a quotation mark or other punctuation
        Pattern sentenceDelimiters = Pattern.compile("(?<=[.!?])\\s+(?=[A-Z])|(?<=[.!?][\"”’])\\s+(?=[A-Z])");

        // Split the text using the defined regular expression
        String[] sentencesArray = sentenceDelimiters.split(text);

        // Create a list to store the cleaned sentences
        List<String> sentences = new ArrayList<>();

        // Remove any leading or trailing whitespace from each sentence and add it to the list
        for (String sentence : sentencesArray) {
            String trimmedSentence = sentence.trim();
            if (!trimmedSentence.isEmpty()) {
                sentences.add(trimmedSentence);
            }
        }

        // Return the cleaned list of sentences
        return sentences;
    }
}
