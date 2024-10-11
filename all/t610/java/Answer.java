package org.real.temp;

import java.util.Objects;

public class Answer {
    private String name;
    private int age;

    // Constructor
    public Answer(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;

        // Calculate hash code based on name
        result = prime * result + (name == null ? 0 : name.hashCode());

        // Calculate hash code based on age
        result = prime * result + age;

        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true; // Check if the same reference
        if (obj == null || getClass() != obj.getClass()) return false; // Check null and class type

        Answer other = (Answer) obj; // Cast to Answer

        // Compare name and age for equality
        return Objects.equals(name, other.name) && age == other.age;
    }
}
