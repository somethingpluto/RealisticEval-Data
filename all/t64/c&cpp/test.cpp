TEST_CASE("CSV to SQL Conversion", "[csv_to_sql]") {
    SECTION("Empty CSV File") {
        const std::string filePath = "path/to/empty.csv";
        std::ofstream ofs(filePath);
        ofs.close();

        REQUIRE(csvToSqlInsert(filePath).empty());

        // Clean up
        std::remove(filePath.c_str());
    }

    SECTION("Valid CSV File") {
        const std::string filePath = "path/to/valid.csv";
        std::ofstream ofs(filePath);
        ofs << "id,name\n1,Alice\n2,Bob";
        ofs.close();

        std::string expectedSql = "INSERT INTO table_name (id, name) VALUES (1, 'Alice'), (2, 'Bob');\n";
        REQUIRE(csvToSqlInsert(filePath) == expectedSql);

        // Clean up
        std::remove(filePath.c_str());
    }
}