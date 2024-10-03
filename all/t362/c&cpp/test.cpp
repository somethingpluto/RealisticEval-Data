struct Rectangle {
    int x1, y1; // Bottom-left corner (x1, y1)
    int x2, y2; // Top-right corner (x2, y2)
};

TEST_CASE("Calculate overlap area of two rectangles") {
    // Test case 1: No overlap
    Rectangle rect1 = {0, 0, 1, 1};
    Rectangle rect2 = {2, 2, 3, 3};
    REQUIRE(calculateOverlapArea(rect1, rect2) == 0);

    // Test case 2: Partial overlap
    Rectangle rect3 = {0, 0, 3, 3};
    Rectangle rect4 = {2, 1, 4, 4};
    REQUIRE(calculateOverlapArea(rect3, rect4) == 1); // Overlap area should be 1

    // Test case 3: Full containment
    Rectangle rect5 = {0, 0, 4, 4};
    Rectangle rect6 = {1, 1, 2, 2};
    REQUIRE(calculateOverlapArea(rect5, rect6) == 1); // Overlap area should be 1

    // Test case 4: Edge touching (no area)
    Rectangle rect7 = {0, 0, 1, 1};
    Rectangle rect8 = {1, 0, 2, 1};
    REQUIRE(calculateOverlapArea(rect7, rect8) == 0); // No overlap

    // Test case 5: Full overlap
    Rectangle rect9 = {0, 0, 2, 2};
    Rectangle rect10 = {0, 0, 2, 2};
    REQUIRE(calculateOverlapArea(rect9, rect10) == 4); // Overlap area should be 4

    // Test case 6: Overlap at corners (no area)
    Rectangle rect11 = {0, 0, 1, 1};
    Rectangle rect12 = {1, 1, 2, 2};
    REQUIRE(calculateOverlapArea(rect11, rect12) == 0); // No overlap
}