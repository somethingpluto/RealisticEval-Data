TEST_CASE("createCircleOfFifths", "[CircleOfFifths]") {
    SECTION("should return 12 notes in the circle") {
        auto result = createCircleOfFifths("C");
        REQUIRE(result.size() == 12);
    }

    SECTION("should start with the given starting note") {
        std::string startingNote = "G";
        auto result = createCircleOfFifths(startingNote);
        REQUIRE(result[0] == startingNote);
    }

    SECTION("should correctly generate the Circle of Fifths starting from C") {
        auto result = createCircleOfFifths("C");
        std::vector<std::string> expectedCircle = {"C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "E#"};
        REQUIRE(result == expectedCircle);
    }

    SECTION("should correctly generate the Circle of Fifths starting from G") {
        auto result = createCircleOfFifths("G");
        std::vector<std::string> expectedCircle = {"G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "E#", "B#"};
        REQUIRE(result == expectedCircle);
    }

    SECTION("should correctly generate the Circle of Fifths starting from F") {
        auto result = createCircleOfFifths("F");
        std::vector<std::string> expectedCircle = {"F", "C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#"};
        REQUIRE(result == expectedCircle);
    }
}