package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.List;

public class Tester {

    private final Answer answer = new Answer();

    @Test
    public void testSimpleAddition() {
        String expression = "2 + 2";
        List<String> result = answer.parseExpression(expression);
        assertEquals(List.of("2", "+", "2"), result);
    }

    @Test
    public void testComplexExpression() {
        String expression = "3 + 5 * (2 - 8)";
        List<String> result = answer.parseExpression(expression);
        assertEquals(List.of("3", "+", "5", "*", "(", "2", "-", "8", ")"), result);
    }

    @Test
    public void testNegativeNumbers() {
        String expression = "-1 + 4 - 5";
        List<String> result = answer.parseExpression(expression);
        assertEquals(List.of("-", "1", "+", "4", "-", "5"), result);
    }

    @Test
    public void testDecimals() {
        String expression = "3.5 + 2.1";
        List<String> result = answer.parseExpression(expression);
        assertEquals(List.of("3.5", "+", "2.1"), result);
    }

    @Test
    public void testOperatorsOnly() {
        String expression = "+ - * /";
        List<String> result = answer.parseExpression(expression);
        assertEquals(List.of("+", "-", "*", "/"), result);
    }

    @Test
    public void testEmptyExpression() {
        String expression = "";
        List<String> result = answer.parseExpression(expression);
        assertTrue(result.isEmpty());
    }

    @Test
    public void testSingleNumber() {
        String expression = "42";
        List<String> result = answer.parseExpression(expression);
        assertEquals(List.of("42"), result);
    }
}
