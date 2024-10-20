TEST_CASE("Test a strong password that meets all criteria", "[valid_password]") {
    REQUIRE(is_strong_password("StrongPass1"));
}

TEST_CASE("Test a password missing a lowercase letter", "[missing_lowercase]") {
    REQUIRE_FALSE(is_strong_password("STRONGPASS1"));
}

TEST_CASE("Test a password missing an uppercase letter", "[missing_uppercase]") {
    REQUIRE_FALSE(is_strong_password("strongpass1"));
}

TEST_CASE("Test a password missing a number", "[missing_number]") {
    REQUIRE_FALSE(is_strong_password("StrongPassword"));
}

TEST_CASE("Test a password that is too short", "[too_short]") {
    REQUIRE_FALSE(is_strong_password("Short1"));
}

TEST_CASE("Test a password that includes special characters but is still strong", "[valid_with_special_characters]") {
    REQUIRE(is_strong_password("Strong!Password1"));
}