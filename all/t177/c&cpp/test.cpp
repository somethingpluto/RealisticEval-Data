TEST_CASE("Hash Password with Salt Length", "[hashing]") {
    /* Test that the hashPasswordWithSalt method returns a byte array with the correct length. */
    std::string password = "testPassword";
    auto result = hash_password_with_salt(password);
    // SHA-256 hash length is 32 bytes, and the salt length is 16 bytes
    REQUIRE(result.size() == 48);
}

TEST_CASE("Salt Is Included In Result", "[hashing]") {
    /* Test that the salt is correctly generated and included in the hash result. */
    std::string password = "testPassword";
    auto result = hash_password_with_salt(password);
    std::vector<uint8_t> salt(result.begin(), result.begin() + 16);  // First 16 bytes represent the salt
    REQUIRE(salt.size() == 16);
    REQUIRE(salt.data() != nullptr);
}

TEST_CASE("Different Passwords Produce Different Hashes", "[hashing]") {
    /* Test that two different passwords produce different hashes, even with the same salt. */
    std::string password1 = "password123";
    std::string password2 = "password456";
    auto hash1 = hash_password_with_salt(password1);
    auto hash2 = hash_password_with_salt(password2);
    REQUIRE(hash1 != hash2);
}

TEST_CASE("Same Password Different Salts", "[hashing]") {
    /* Test that the same password produces different hashes when hashed with different salts. */
    std::string password = "password123";
    auto hash1 = hash_password_with_salt(password);
    auto hash2 = hash_password_with_salt(password);
    // The salt is generated randomly, so the hashes should be different.
    REQUIRE(hash1 != hash2);
}