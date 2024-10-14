#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <vector>

struct NoteSeparation {
    std::vector<int> octaveNotes;
    std::vector<int> rootNotes;
};

NoteSeparation separateOctaveAndRoot(const std::vector<int>& midiNotes);

TEST_CASE("separateOctaveAndRoot") {
    SECTION("correctly separates MIDI notes into octaves and root notes") {
        std::vector<int> midiNotes = {60, 61, 62};  // C4, C#4, D4
        NoteSeparation expected = {{5, 5, 5}, {0, 1, 2}};  // Expected output
        REQUIRE(separateOctaveAndRoot(midiNotes) == expected);
    }

    SECTION("handles single MIDI note input") {
        std::vector<int> midiNotes = {24};  // C1
        NoteSeparation expected = {{2}, {0}};  // Expected output
        REQUIRE(separateOctaveAndRoot(midiNotes) == expected);
    }

    SECTION("returns empty arrays for an empty input array") {
        std::vector<int> midiNotes = {};
        NoteSeparation expected = {{}, {}};  // Expected output
        REQUIRE(separateOctaveAndRoot(midiNotes) == expected);
    }

    SECTION("throws an error for invalid input types") {
        REQUIRE_THROWS_AS(separateOctaveAndRoot({"not an array"}), std::invalid_argument);
        REQUIRE_THROWS_AS(separateOctaveAndRoot({3.14}), std::invalid_argument);
    }

    SECTION("handles MIDI notes from different octaves") {
        std::vector<int> midiNotes = {12, 25, 37};  // C1, C#2, D#3
        NoteSeparation expected = {{1, 2, 3}, {0, 1, 1}};  // Expected output
        REQUIRE(separateOctaveAndRoot(midiNotes) == expected);
    }
}