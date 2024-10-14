TEST_CASE("Test cases for point inside triangle", "[point_inside_triangle]") {
    SECTION("Test case where point is inside the triangle") {
        double triangle_vertices[] = {0, 0, 5, 0, 2.5, 5};
        double point[] = {2.5, 2};  // Inside the triangle
        REQUIRE(is_point_inside_triangle(point[0], point[1], triangle_vertices[0], triangle_vertices[1], triangle_vertices[2], triangle_vertices[3], triangle_vertices[4], triangle_vertices[5]));
    }

    SECTION("Test case where point is on the edge of the triangle") {
        double triangle_vertices[] = {0, 0, 5, 0, 2.5, 5};
        double point[] = {2.5, 0};  // On the edge of the triangle
        REQUIRE(is_point_inside_triangle(point[0], point[1], triangle_vertices[0], triangle_vertices[1], triangle_vertices[2], triangle_vertices[3], triangle_vertices[4], triangle_vertices[5]));
    }

    SECTION("Test case where point is outside the triangle") {
        double triangle_vertices[] = {0, 0, 5, 0, 2.5, 5};
        double point[] = {6, 2};  // Outside the triangle
        REQUIRE_FALSE(is_point_inside_triangle(point[0], point[1], triangle_vertices[0], triangle_vertices[1], triangle_vertices[2], triangle_vertices[3], triangle_vertices[4], triangle_vertices[5]));
    }

    SECTION("Test case where point is at one of the triangle's vertices") {
        double triangle_vertices[] = {0, 0, 5, 0, 2.5, 5};
        double point[] = {0, 0};  // At the vertex of the triangle
        REQUIRE(is_point_inside_triangle(point[0], point[1], triangle_vertices[0], triangle_vertices[1], triangle_vertices[2], triangle_vertices[3], triangle_vertices[4], triangle_vertices[5]));
    }
}