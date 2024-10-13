TEST_CASE("Test Haversine Distance", "[haversine_distance]") {
    SECTION("Same point should return a distance of 0") {
        double lat = 52.2296756;
        double lon = 21.0122287;
        double result = haversine_distance(lat, lon, lat, lon);
        REQUIRE(std::abs(result - 0.0) < 1e-6);
    }

    SECTION("Points that are very close together (few meters apart)") {
        double lat1 = 52.2296756;
        double lon1 = 21.0122287;  // Warsaw, Poland
        double lat2 = 52.2296756;
        double lon2 = 21.0122297;  // Very close to the previous point
        double result = haversine_distance(lat1, lon1, lat2, lon2);
        REQUIRE(std::abs(result - 0.0001) < 1e-4);
    }

    SECTION("Points that are far apart") {
        double lat1 = 52.2296756;
        double lon1 = 21.0122287;  // Warsaw, Poland
        double lat2 = 41.8919300;
        double lon2 = 12.5113300;  // Rome, Italy
        double result = haversine_distance(lat1, lon1, lat2, lon2);
        REQUIRE(std::abs(result - 1315.514) < 1e-2);
    }

    SECTION("Points on the equator") {
        double lat1 = 0.0;
        double lon1 = 0.0;  // Gulf of Guinea (Equator and Prime Meridian intersection)
        double lat2 = 0.0;
        double lon2 = 90.0;  // On the Equator, 90 degrees east
        double result = haversine_distance(lat1, lon1, lat2, lon2);
        REQUIRE(std::abs(result - 10007.54) < 1e-2);
    }

    SECTION("Distance from North Pole to South Pole") {
        double lat1 = 90.0;
        double lon1 = 0.0;  // North Pole
        double lat2 = -90.0;
        double lon2 = 0.0;  // South Pole
        double result = haversine_distance(lat1, lon1, lat2, lon2);
        REQUIRE(std::abs(result - 20015.09) < 1e-2);
    }
}