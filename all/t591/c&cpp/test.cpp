TEST_CASE("Color RGB Values", "[Color]") {
    Color color;

    SECTION("Verify RGB values for Red") {
        auto rgb = color.getColor(Color::RED);
        REQUIRE(std::get<0>(rgb) == 255);
        REQUIRE(std::get<1>(rgb) == 0);
        REQUIRE(std::get<2>(rgb) == 0);
    }

    SECTION("Verify RGB values for Green") {
        auto rgb = color.getColor(Color::GREEN);
        REQUIRE(std::get<0>(rgb) == 0);
        REQUIRE(std::get<1>(rgb) == 255);
        REQUIRE(std::get<2>(rgb) == 0);
    }

    SECTION("Verify RGB values for Blue") {
        auto rgb = color.getColor(Color::BLUE);
        REQUIRE(std::get<0>(rgb) == 0);
        REQUIRE(std::get<1>(rgb) == 0);
        REQUIRE(std::get<2>(rgb) == 255);
    }

    SECTION("Verify RGB values for Yellow") {
        auto rgb = color.getColor(Color::YELLOW);
        REQUIRE(std::get<0>(rgb) == 255);
        REQUIRE(std::get<1>(rgb) == 255);
        REQUIRE(std::get<2>(rgb) == 0);
    }

    SECTION("Verify RGB values for Magenta") {
        auto rgb = color.getColor(Color::MAGENTA);
        REQUIRE(std::get<0>(rgb) == 255);
        REQUIRE(std::get<1>(rgb) == 0);
        REQUIRE(std::get<2>(rgb) == 255);
    }

    SECTION("Verify RGB values for Cyan") {
        auto rgb = color.getColor(Color::CYAN);
        REQUIRE(std::get<0>(rgb) == 0);
        REQUIRE(std::get<1>(rgb) == 255);
        REQUIRE(std::get<2>(rgb) == 255);
    }

    SECTION("Verify RGB values for White") {
        auto rgb = color.getColor(Color::WHITE);
        REQUIRE(std::get<0>(rgb) == 255);
        REQUIRE(std::get<1>(rgb) == 255);
        REQUIRE(std::get<2>(rgb) == 255);
    }

    SECTION("Verify RGB values for Black") {
        auto rgb = color.getColor(Color::BLACK);
        REQUIRE(std::get<0>(rgb) == 0);
        REQUIRE(std::get<1>(rgb) == 0);
        REQUIRE(std::get<2>(rgb) == 0);
    }

    SECTION("Verify RGB values for Orange") {
        auto rgb = color.getColor(Color::ORANGE);
        REQUIRE(std::get<0>(rgb) == 255);
        REQUIRE(std::get<1>(rgb) == 165);
        REQUIRE(std::get<2>(rgb) == 0);
    }

    SECTION("Verify RGB values for Purple") {
        auto rgb = color.getColor(Color::PURPLE);
        REQUIRE(std::get<0>(rgb) == 128);
        REQUIRE(std::get<1>(rgb) == 0);
        REQUIRE(std::get<2>(rgb) == 128);
    }

    SECTION("Verify RGB values for Pink") {
        auto rgb = color.getColor(Color::PINK);
        REQUIRE(std::get<0>(rgb) == 255);
        REQUIRE(std::get<1>(rgb) == 192);
        REQUIRE(std::get<2>(rgb) == 203);
    }

    SECTION("Verify RGB values for Brown") {
        auto rgb = color.getColor(Color::BROWN);
        REQUIRE(std::get<0>(rgb) == 165);
        REQUIRE(std::get<1>(rgb) == 42);
        REQUIRE(std::get<2>(rgb) == 42);
    }
}