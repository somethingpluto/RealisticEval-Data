TEST_CASE("changedClef", "[changedClef]") {
    SECTION("should insert the clef at the correct position when the clef is not specified (default to 'bass')") {
        std::string abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n";
        std::string result = changedClef(abc);
        std::string expected = "X:1\nT:Test Tune\nK:C clef=bass\nC D E F|G A B c|\n";
        REQUIRE(result == expected);
    }

    SECTION("should insert the clef at the correct position when a specific clef is provided") {
        std::string abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n";
        std::string result = changedClef(abc, "treble");
        std::string expected = "X:1\nT:Test Tune\nK:C clef=treble\nC D E F|G A B c|\n";
        REQUIRE(result == expected);
    }

    SECTION("should handle cases where there is no newline after the key signature") {
        std::string abc = "X:1\nT:Test Tune\nK:C";
        std::string result = changedClef(abc, "alto");
        std::string expected = "X:1\nT:Test Tune\nK:C clef=alto";
        REQUIRE(result == expected);
    }

    SECTION("should not alter the ABC notation if the key signature is not found") {
        std::string abc = "X:1\nT:Test Tune\nC D E F|G A B c|\n";
        std::string result = changedClef(abc, "tenor");
        REQUIRE(result == abc); // Expect the original string to be returned unchanged
    }

    SECTION("should correctly handle ABC notation with multiple key signatures") {
        std::string abc = "X:1\nT:Test Tune\nK:G\nG A B c|\nK:D\nD E F# G|\n";
        std::string result = changedClef(abc, "baritone");
        std::string expected = "X:1\nT:Test Tune\nK:G clef=baritone\nG A B c|\nK:D\nD E F# G|\n";
        REQUIRE(result == expected);
    }
}