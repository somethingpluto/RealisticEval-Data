package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.ArrayList;
import java.util.List;

public class Answer {
    public List<String> findPlaceholders(String text) {
        Pattern pattern = Pattern.compile("\\{\\{\\s*([^{}]+)\\s*\\}\\}");
        Matcher matcher = pattern.matcher(text);

        List<String> placeholders = new ArrayList<>();
        while (matcher.find()) {
            placeholders.add(matcher.group(1));
        }

        return placeholders;
    }
}