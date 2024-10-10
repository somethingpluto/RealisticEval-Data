package org.real.temp;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {
    public static List<String> codeBlockRemover(String markdownString) {
        // Regular expression pattern to match code blocks in markdown
        Pattern pattern = Pattern.compile("(```.*?```)", Pattern.DOTALL);
        Matcher matcher = pattern.matcher(markdownString);

        List<String> codeBlocks = new ArrayList<>();

        while (matcher.find()) {
            String codeBlock = matcher.group(1);
            // Remove the triple backticks that enclose the code block
            codeBlock = codeBlock.replaceFirst("^`{3}", "").replaceAll("`{3}$", "");
            codeBlocks.add(codeBlock.trim());
        }

        return codeBlocks;
    }
}