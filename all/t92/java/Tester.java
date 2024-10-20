package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testDecodesStandardHtmlEntities() {
        String input = "The &amp; symbol should become an &quot;and&quot; sign.";
        String expected = "The & symbol should become an \"and\" sign.";
        assertEquals(expected, replaceHtmlEntities(input));
    }

    @Test
    public void testReturnsEmptyStringForEmptyInput() {
        String input = "";
        String expected = "";
        assertEquals(expected, replaceHtmlEntities(input));
    }

    @Test
    public void testDecodesMultipleDifferentEntitiesInOneString() {
        String input = "&lt;div&gt;Hello &amp; Welcome to the &apos;World&apos;!&lt;/div&gt;";
        String expected = "<div>Hello & Welcome to the 'World'!</div>";
        assertEquals(expected, replaceHtmlEntities(input));
    }

    @Test
    public void testHandlesStringsWithNoEntities() {
        String input = "Just a normal string without entities.";
        String expected = "Just a normal string without entities.";
        assertEquals(expected, replaceHtmlEntities(input));
    }
}