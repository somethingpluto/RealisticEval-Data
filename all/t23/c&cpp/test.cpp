TEST_CASE("Test Line Segment Intersection", "[intersection]") {
    SECTION("Segments do not intersect") {
        auto seg1 = std::make_pair(std::make_pair(0.0, 0.0), std::make_pair(1.0, 1.0));
        auto seg2 = std::make_pair(std::make_pair(0.0, 1.0), std::make_pair(1.0, 0.0));
        
        auto result = getLineSegmentIntersection(seg1, seg2);
        
        REQUIRE(result.first == Approx(NAN));
        REQUIRE(result.second == Approx(NAN));
    }

    SECTION("Segments intersect at a single point") {
        auto seg1 = std::make_pair(std::make_pair(0.0, 0.0), std::make_pair(1.0, 1.0));
        auto seg2 = std::make_pair(std::make_pair(1.0, 0.0), std::make_pair(0.0, 1.0));
        
        auto result = getLineSegmentIntersection(seg1, seg2);
        
        REQUIRE(result.first == Approx(0.5));
        REQUIRE(result.second == Approx(0.5));
    }
    
    SECTION("Segments are collinear but do not intersect") {
        auto seg1 = std::make_pair(std::make_pair(0.0, 0.0), std::make_pair(1.0, 1.0));
        auto seg2 = std::make_pair(std::make_pair(-1.0, -1.0), std::make_pair(0.0, 0.0));
        
        auto result = getLineSegmentIntersection(seg1, seg2);
        
        REQUIRE(result.first == Approx(NAN));
        REQUIRE(result.second == Approx(NAN));
    }
}