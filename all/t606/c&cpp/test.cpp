TEST_CASE("Calculate Steering Angle Tests") {
    const double wheelbase = 2.5; // Setting wheelbase constant for all tests

    SECTION("Normal case") {
        double angularVelocity = 1.0; // radians/second
        double speed = 10.0;          // meters/second
        double expectedAngle = atan((angularVelocity * wheelbase) / speed);
        REQUIRE(calculateSteeringAngle(angularVelocity, speed, wheelbase) == Approx(expectedAngle));
    }

    SECTION("Zero speed") {
        double angularVelocity = 1.0; // radians/second
        double speed = 0.0;           // meters/second
        REQUIRE_THROWS_AS(calculateSteeringAngle(angularVelocity, speed, wheelbase), std::invalid_argument);
    }

    SECTION("Negative speed") {
        double angularVelocity = 1.0; // radians/second
        double speed = -5.0;          // meters/second
        REQUIRE_THROWS_AS(calculateSteeringAngle(angularVelocity, speed, wheelbase), std::invalid_argument);
    }

    SECTION("Zero angular velocity") {
        double angularVelocity = 0.0; // radians/second
        double speed = 10.0;          // meters/second
        double expectedAngle = 0.0;   // Steering angle should be zero
        REQUIRE(calculateSteeringAngle(angularVelocity, speed, wheelbase) == Approx(expectedAngle));
    }

    SECTION("Large values") {
        double angularVelocity = 100.0; // radians/second
        double speed = 1000.0;          // meters/second
        double expectedAngle = atan((angularVelocity * wheelbase) / speed);
        REQUIRE(calculateSteeringAngle(angularVelocity, speed, wheelbase) == Approx(expectedAngle));
    }

    SECTION("High angular velocity") {
        double angularVelocity = 10.0; // radians/second
        double speed = 1.0;             // meters/second
        double expectedAngle = atan((angularVelocity * wheelbase) / speed);
        REQUIRE(calculateSteeringAngle(angularVelocity, speed, wheelbase) == Approx(expectedAngle));
    }
}