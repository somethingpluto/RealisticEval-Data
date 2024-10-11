TEST_CASE("Replace Phone Numbers", "[replace_phone_numbers]") {
    SECTION("Single Phone Number") {
        REQUIRE(replace_phone_numbers("Call me at 123-456-7890.") == "Call me at [PHONE_NUM].");
    }

    SECTION("Multiple Phone Numbers") {
        REQUIRE(replace_phone_numbers("Contact us at 123-456-7890 or 987-654-3210.") 
                == "Contact us at [PHONE_NUM] or [PHONE_NUM].");
    }

    SECTION("No Phone Numbers") {
        REQUIRE(replace_phone_numbers("This is just a normal message.") 
                == "This is just a normal message.");
    }

    SECTION("Phone Number with Different Format") {
        REQUIRE(replace_phone_numbers("Reach out at (123) 456-7890.") 
                == "Reach out at [PHONE_NUM].");
    }
}