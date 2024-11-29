package org.real.temp;

import org.junit.Test;
import org.junit.Assert;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSimpleDictionary() {
        Map<String, Object> data = new HashMap<>();
        data.put("name", "Alice".getBytes());
        data.put("age", "30");

        Map<String, Object> expected = new HashMap<>();
        expected.put("name", "Alice");
        expected.put("age", 30);

        Assert.assertEquals(expected, handleNestedData(data));
    }

    @Test
    public void testNestedDictionary() {
        Map<String, Object> nestedDetails = new HashMap<>();
        nestedDetails.put("age", "25");
        nestedDetails.put("height", "175.5");

        Map<String, Object> nestedUser = new HashMap<>();
        nestedUser.put("name", "Bob".getBytes());
        nestedUser.put("details", nestedDetails);

        Map<String, Object> data = new HashMap<>();
        data.put("user", nestedUser);

        Map<String, Object> expectedDetails = new HashMap<>();
        expectedDetails.put("age", 25);
        expectedDetails.put("height", 175.5);

        Map<String, Object> expectedUser = new HashMap<>();
        expectedUser.put("name", "Bob");
        expectedUser.put("details", expectedDetails);

        Map<String, Object> expected = new HashMap<>();
        expected.put("user", expectedUser);

        Assert.assertEquals(expected, handleNestedData(data));
    }

    @Test
    public void testListOfMixedDataTypes() {
        List<Object> data = Arrays.asList("100", "200".getBytes(), 300.0, "400.5");

        List<Object> expected = Arrays.asList(100, "200", 300.0, 400.5);

        Assert.assertEquals(expected, handleNestedData(data));
    }


    @Test
    public void testComplexNestedStructure() {
        Map<String, Object> charlieScores = new HashMap<>();
        charlieScores.put("name", "Charlie".getBytes());
        charlieScores.put("scores", Arrays.asList("1000", "2000.2"));

        Map<String, Object> daisySkills = new HashMap<>();
        daisySkills.put("name", "Daisy".getBytes());
        daisySkills.put("skills", Arrays.asList("Coding".getBytes(), "Design".getBytes()));
        daisySkills.put("age", "22");

        List<Object> team = Arrays.asList(charlieScores, daisySkills);

        Map<String, Object> data = new HashMap<>();
        data.put("team", team);

        Map<String, Object> expectedCharlieScores = new HashMap<>();
        expectedCharlieScores.put("name", "Charlie");
        expectedCharlieScores.put("scores", Arrays.asList(1000, 2000.2));

        Map<String, Object> expectedDaisySkills = new HashMap<>();
        expectedDaisySkills.put("name", "Daisy");
        expectedDaisySkills.put("skills", Arrays.asList("Coding", "Design"));
        expectedDaisySkills.put("age", 22);

        List<Object> expectedTeam = Arrays.asList(expectedCharlieScores, expectedDaisySkills);

        Map<String, Object> expected = new HashMap<>();
        expected.put("team", expectedTeam);

        Assert.assertEquals(expected, handleNestedData(data));
    }
}