TEST_CASE_METHOD(TestAnswer, "Test Modify Line Success") {
    modifyLineInFile(TEST_FILE, 2, "Updated Line 2");
    
    std::ifstream reader(TEST_FILE);
    std::string line;
    
    REQUIRE(std::getline(reader, line));
    REQUIRE(line == "Line 1");
    
    REQUIRE(std::getline(reader, line));
    REQUIRE(line == "Updated Line 2");
    
    REQUIRE(std::getline(reader, line));
    REQUIRE(line == "Line 3");
}

TEST_CASE_METHOD(TestAnswer, "Test Modify First Line") {
    modifyLineInFile(TEST_FILE, 1, "Updated Line 1");
    
    std::ifstream reader(TEST_FILE);
    std::string line;
    
    REQUIRE(std::getline(reader, line));
    REQUIRE(line == "Updated Line 1");
    
    REQUIRE(std::getline(reader, line));
    REQUIRE(line == "Line 2");
    
    REQUIRE(std::getline(reader, line));
    REQUIRE(line == "Line 3");
}

TEST_CASE_METHOD(TestAnswer, "Test Modify Last Line") {
    modifyLineInFile(TEST_FILE, 3, "Updated Line 3");
    
    std::ifstream reader(TEST_FILE);
    std::string line;
    
    REQUIRE(std::getline(reader, line));
    REQUIRE(line == "Line 1");
    
    REQUIRE(std::getline(reader, line));
    REQUIRE(line == "Line 2");
    
    REQUIRE(std::getline(reader, line));
    REQUIRE(line == "Updated Line 3");
}

TEST_CASE_METHOD(TestAnswer, "Test Modify Non-Existent Line") {
    REQUIRE_THROWS_AS(modifyLineInFile(TEST_FILE, 4, "Should Fail"), std::exception);
}

TEST_CASE_METHOD(TestAnswer, "Test Modify Negative Line Number") {
    REQUIRE_THROWS_AS(modifyLineInFile(TEST_FILE, 0, "Should Fail"), std::exception);
}