// Test case for valid inputs with expected BMI value
TEST_CASE("Valid BMI calculations") {
    SECTION("Normal weight") {
        REQUIRE(calculateBMI(70, 1.75) == Approx(22.86).epsilon(0.01)); // 70 kg, 1.75 m
    }

    SECTION("Underweight") {
        REQUIRE(calculateBMI(50, 1.75) == Approx(16.33).epsilon(0.01)); // 50 kg, 1.75 m
    }

    SECTION("Overweight") {
        REQUIRE(calculateBMI(80, 1.75) == Approx(26.12).epsilon(0.01)); // 80 kg, 1.75 m
    }

    SECTION("Obesity") {
        REQUIRE(calculateBMI(100, 1.75) == Approx(32.65).epsilon(0.01)); // 100 kg, 1.75 m
    }
}

// Test case for invalid inputs
TEST_CASE("Invalid BMI calculations") {
    SECTION("Negative weight") {
        REQUIRE_THROWS_AS(calculateBMI(-70, 1.75), std::invalid_argument); // Negative weight
    }

    SECTION("Zero height") {
        REQUIRE_THROWS_AS(calculateBMI(70, 0), std::invalid_argument); // Zero height
    }

    SECTION("Negative height") {
        REQUIRE_THROWS_AS(calculateBMI(70, -1.75), std::invalid_argument); // Negative height
    }
}