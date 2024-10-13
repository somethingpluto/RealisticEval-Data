TEST_CASE("TestCsvToSqlInsert", "[csv_to_sql_insert]") {
    // Create sample CSV files for testing
    std::map<std::string, std::string> test_files = {
        {"test1.csv", "id,name,age\n1,Alice,30\n2,Bob,25"},
        {"test2.csv", "product_id,product_name,price\n101,Widget,9.99\n102,Gadget,12.49"},
        {"test3.csv", "user_id,email\n3,test@example.com\n4,user@domain.com"},
        {"test4.csv", "order_id,order_date,total\n1001,2024-09-01,59.99"},
        {"test5.csv", "quote_id,quote\n1,\"It's a beautiful day.\"\n2,\"She said, \"\"Hello!\"\"\""}
    };

    // Create the files on disk
    for (const auto& [filename, content] : test_files) {
        std::ofstream file(filename);
        file << content;
        file.close();
    }

    SECTION("test_simple_csv") {
        std::string expected_sql = (
            "INSERT INTO test1 (id, name, age) VALUES ('1', 'Alice', '30');\n"
            "INSERT INTO test1 (id, name, age) VALUES ('2', 'Bob', '25');"
        );
        std::string result = csv_to_sql_insert("test1.csv");
        REQUIRE(result == expected_sql);
    }

    SECTION("test_product_csv") {
        std::string expected_sql = (
            "INSERT INTO test2 (product_id, product_name, price) VALUES ('101', 'Widget', '9.99');\n"
            "INSERT INTO test2 (product_id, product_name, price) VALUES ('102', 'Gadget', '12.49');"
        );
        std::string result = csv_to_sql_insert("test2.csv");
        REQUIRE(result == expected_sql);
    }

    SECTION("test_email_csv") {
        std::string expected_sql = (
            "INSERT INTO test3 (user_id, email) VALUES ('3', 'test@example.com');\n"
            "INSERT INTO test3 (user_id, email) VALUES ('4', 'user@domain.com');"
        );
        std::string result = csv_to_sql_insert("test3.csv");
        REQUIRE(result == expected_sql);
    }

    SECTION("test_date_and_decimal_csv") {
        std::string expected_sql = (
            "INSERT INTO test4 (order_id, order_date, total) VALUES ('1001', '2024-09-01', '59.99');"
        );
        std::string result = csv_to_sql_insert("test4.csv");
        REQUIRE(result == expected_sql);
    }

    // Remove the test files after tests
    for (const auto& filename : test_files) {
        fs::remove(filename.first);
    }
}