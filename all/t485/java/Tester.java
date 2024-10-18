package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test class for the prepareQuery function.
 */
public class Tester {

    /**
     * Tests the prepareQuery function with valid named parameters.
     */
    @Test
    public void testValidNamedParameters() {
        String sqlQuery = "SELECT * FROM users WHERE id = $user_id AND status = $status";
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("user_id", 42);
        parameters.put("status", "active");

        Pair<String, List<Object>> result = Answer.prepareQuery(sqlQuery, parameters);
        String newSql = result.getFirst();
        List<Object> valueList = result.getSecond();

        String expectedSql = "SELECT * FROM users WHERE id = $1 AND status = $2";
        List<Object> expectedValues = Arrays.asList(42, "active");

        assertEquals(expectedSql, newSql);
        assertEquals(expectedValues, valueList);
    }

    /**
     * Tests the prepareQuery function with missing parameters.
     */
    @Test
    public void testMissingParameters() {
        String sqlQuery = "SELECT * FROM users WHERE id = $user_id AND status = $status";
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("user_id", 42);  // 'status' is missing

        Pair<String, List<Object>> result = Answer.prepareQuery(sqlQuery, parameters);
        String newSql = result.getFirst();
        List<Object> valueList = result.getSecond();

        String expectedSql = "SELECT * FROM users WHERE id = $1 AND status = $2";
        List<Object> expectedValues = Arrays.asList(42);  // 'status' is not included

        assertEquals(expectedSql, newSql);
        assertEquals(expectedValues, valueList);
    }

    /**
     * Tests the prepareQuery function with no parameters.
     */
    @Test
    public void testNoParameters() {
        String sqlQuery = "SELECT * FROM users";
        Map<String, Object> parameters = new HashMap<>();  // No parameters provided

        Pair<String, List<Object>> result = Answer.prepareQuery(sqlQuery, parameters);
        String newSql = result.getFirst();
        List<Object> valueList = result.getSecond();

        String expectedSql = "SELECT * FROM users";
        List<Object> expectedValues = new ArrayList<>();

        assertEquals(expectedSql, newSql);
        assertEquals(expectedValues, valueList);
    }

    /**
     * Tests the prepareQuery function with multiple same parameters.
     */
    @Test
    public void testMultipleSameParameters() {
        String sqlQuery = "SELECT * FROM users WHERE id = $user_id AND status = $user_id";
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("user_id", 42);

        Pair<String, List<Object>> result = Answer.prepareQuery(sqlQuery, parameters);
        String newSql = result.getFirst();
        List<Object> valueList = result.getSecond();

        String expectedSql = "SELECT * FROM users WHERE id = $1 AND status = $1";
        List<Object> expectedValues = Arrays.asList(42);  // Only one value for 'user_id'

        assertEquals(expectedSql, newSql);
        assertEquals(expectedValues, valueList);
    }

    /**
     * Tests the prepareQuery function with special characters in parameters.
     */
    @Test
    public void testSpecialCharactersInParameter() {
        String sqlQuery = "INSERT INTO users (name, email) VALUES ($name, $email)";
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("name", "John Doe");
        parameters.put("email", "john.doe@example.com");

        Pair<String, List<Object>> result = Answer.prepareQuery(sqlQuery, parameters);
        String newSql = result.getFirst();
        List<Object> valueList = result.getSecond();

        String expectedSql = "INSERT INTO users (name, email) VALUES ($1, $2)";
        List<Object> expectedValues = Arrays.asList("John Doe", "john.doe@example.com");

        assertEquals(expectedSql, newSql);
        assertEquals(expectedValues, valueList);
    }
}
