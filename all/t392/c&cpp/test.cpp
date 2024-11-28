TEST_CASE("Test Look and Say Sequence", "[look_and_say]") {
    SECTION("Test with a single digit") {
        // Test with a single digit to see if it replicates correctly
        CHECK(look_and_say("1") == "11");
    }

    SECTION("Test a sequence of the same digits") {
        // Test a sequence of the same digits
        CHECK(look_and_say("111") == "31");
    }

    SECTION("Test a sequence with different digits") {
        // Test a sequence with different digits
        CHECK(look_and_say("1211") == "111221");
    }

    SECTION("Test a more complex sequence") {
        // Test a more complex sequence
        CHECK(look_and_say("312211") == "13112221");
    }
}