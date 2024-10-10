TEST_CASE("Calculate bearing", "[calculate_bearing]")
{
    REQUIRE(calculate_bearing(52.2296756, 21.0122287, 41.8919300, 12.5113300) == Approx(158.0));
    REQUIRE(calculate_bearing(-33.8688200, 151.2092960, 37.7749296, -122.4194180) == Approx(135.0));
}