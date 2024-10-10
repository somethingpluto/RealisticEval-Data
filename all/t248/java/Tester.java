package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Before;
import org.junit.Test;

public class Tester {

    private SanitizeData sanitizer;

    @Before
    public void setUp() {
        sanitizer = new SanitizeData();
    }

    @Test
    public void testSanitizeDataWithKeys() {
        // Arrange
        Data data = new Data("John", 30, "secret");
        String[] keysToRemove = {"password"};
        Data expectedResult = new Data("John", 30);

        // Act
        Data result = sanitizer.sanitizeData(data, keysToRemove);

        // Assert
        assertEquals(expectedResult, result);
    }

    @Test
    public void testSanitizeDataNoKeys() {
        // Arrange
        Data data = new Data("John", 30, "secret");
        String[] keysToRemove = {};
        Data expectedResult = new Data("John", 30, "secret");

        // Act
        Data result = sanitizer.sanitizeData(data, keysToRemove);

        // Assert
        assertEquals(expectedResult, result);
    }

    // Helper classes for testing
    public static class Data {
        private String name;
        private int age;
        private String password;

        public Data(String name, int age, String password) {
            this.name = name;
            this.age = age;
            this.password = password;
        }

        public Data(String name, int age) {
            this.name = name;
            this.age = age;
        }

        // Getters and setters (omitted for brevity)

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Data data = (Data) o;
            return age == data.age && Objects.equals(name, data.name) && Objects.equals(password, data.password);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, age, password);
        }

        @Override
        public String toString() {
            return "Data{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    ", password='" + password + '\'' +
                    '}';
        }
    }

    public static class SanitizeData {
        public Data sanitizeData(Data data, String[] keysToRemove) {
            Data sanitizedData = new Data(data.getName(), data.getAge());
            for (String key : keysToRemove) {
                if ("password".equals(key)) {
                    sanitizedData.setPassword(null);
                }
            }
            return sanitizedData;
        }
    }
}