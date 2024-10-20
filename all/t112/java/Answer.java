package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    public static String convertHtmlHeadingsToMarkdown(String html) {
        html = html.replaceAll("<h1>(.*?)</h1>", "# $1");
        html = html.replaceAll("<h2>(.*?)</h2>", "## $1");
        html = html.replaceAll("<h3>(.*?)</h3>", "### $1");
        html = html.replaceAll("<h4>(.*?)</h4>", "#### $1");
        html = html.replaceAll("<h5>(.*?)</h5>", "##### $1");
        html = html.replaceAll("<h6>(.*?)</h6>", "###### $1");
        return html;
    }
}