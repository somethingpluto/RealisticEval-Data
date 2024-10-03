TEST_CASE("Ray-Circle Intersection Tests") {
    // Test Case 1: The ray intersects the circle at two points
    {
        Ray ray = {{0, 0}, {1, 1}}; // Origin at (0, 0), direction (1, 1)
        Circle circle = {{3, 3}, 2}; // Circle center at (3, 3), radius 2
        REQUIRE(intersects(ray, circle) == true);
    }

    // Test Case 2: The ray is tangent to the circle (one intersection point)
    {
        Ray ray = {{2, 0}, {0, 1}}; // Origin at (2, 0), direction (0, 1)
        Circle circle = {{2, 2}, 1}; // Circle center at (2, 2), radius 1
        REQUIRE(intersects(ray, circle) == true);
    }

    // Test Case 3: The ray starts inside the circle (one intersection point)
    {
        Ray ray = {{2, 2}, {1, 0}}; // Origin at (2, 2), direction (1, 0)
        Circle circle = {{3, 2}, 1}; // Circle center at (3, 2), radius 1
        REQUIRE(intersects(ray, circle) == true);
    }

    // Test Case 4: The ray originates outside and goes away from the circle (no intersection)
    {
        Ray ray = {{5, 5}, {1, 0}}; // Origin at (5, 5), direction (1, 0)
        Circle circle = {{3, 3}, 1}; // Circle center at (3, 3), radius 1
        REQUIRE(intersects(ray, circle) == false);
    }

    // Test Case 5: The ray is parallel to the line connecting the center of the circle and is outside (no intersection)
    {
        Ray ray = {{0, 3}, {1, 0}}; // Origin at (0, 3), direction (1, 0)
        Circle circle = {{3, 3}, 1}; // Circle center at (3, 3), radius 1
        REQUIRE(intersects(ray, circle) == true);
    }

    // Test Case 6: The ray intersects the circle at one point when passing through the center
    {
        Ray ray = {{3, 0}, {0, 1}}; // Origin at (3, 0), direction (0, 1)
        Circle circle = {{3, 3}, 3}; // Circle center at (3, 3), radius 3
        REQUIRE(intersects(ray, circle) == true);
    }
}