TEST_CASE("Move Emojis to End", "[move_emojis_to_end]") {
    REQUIRE(move_emojis_to_end("") == "");
    REQUIRE(move_emojis_to_end("Hello World!") == "Hello World!");
    REQUIRE(move_emojis_to_end("Hello 🌍!") == "Hello !🌍");
    REQUIRE(move_emojis_to_end("👋 Hello 🌍!") == "Hello !👋🌍");
    REQUIRE(move_emojis_to_end("Hello 🌍👋!") == "Hello !👋🌍");
}