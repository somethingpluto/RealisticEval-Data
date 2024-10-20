TEST_CASE("Test Generate Random String") {

    SECTION("Test length") {
        std::string random_string = generate_random_string();
        REQUIRE(random_string.length() == 25);
    }

    SECTION("Test contains upper case") {
        std::string random_string = generate_random_string();
        bool has_upper_case = std::any_of(random_string.begin(), random_string.end(), [](char c) {
            return std::isupper(static_cast<unsigned char>(c));
        });
        REQUIRE(has_upper_case);
    }

    SECTION("Test contains lower case") {
        std::string random_string = generate_random_string();
        bool has_lower_case = std::any_of(random_string.begin(), random_string.end(), [](char c) {
            return std::islower(static_cast<unsigned char>(c));
        });
        REQUIRE(has_lower_case);
    }

    SECTION("Test randomness") {
        std::string string1 = generate_random_string();
        std::string string2 = generate_random_string();
        REQUIRE(string1 != string2);
    }

    SECTION("Test multiple generations") {
        const int num_tests = 100;
        bool has_upper_case = false;
        bool has_lower_case = false;

        for (int i = 0; i < num_tests; ++i) {
            std::string random_string = generate_random_string();
            has_upper_case |= std::any_of(random_string.begin(), random_string.end(), [](char c) {
                return std::isupper(static_cast<unsigned char>(c));
            });
            has_lower_case |= std::any_of(random_string.begin(), random_string.end(), [](char c) {
                return std::islower(static_cast<unsigned char>(c));
            });
        }

        REQUIRE(has_upper_case);
        REQUIRE(has_lower_case);
    }
}