TEST_CASE("Test TSV to JSONL conversion", "[tsv_to_jsonl]") {
    // Create a temporary directory for testing
    fs::path temp_dir = fs::temp_directory_path() / "test_tsv_to_jsonl";
    fs::create_directory(temp_dir);

    SECTION("Standard TSV") {
        std::string tsv_content = "Name\tAge\tCountry\nAlice\t30\tUSA\nBob\t25\tCanada\n";
        std::string tsv_file = (temp_dir / "test_standard.tsv").string();
        std::string jsonl_file = (temp_dir / "test_standard.jsonl").string();

        std::ofstream tsv(tsv_file);
        tsv << tsv_content;
        tsv.close();

        tsv_to_jsonl(tsv_file, jsonl_file);

        std::ifstream jsonl(jsonl_file);
        std::vector<std::string> lines;
        std::string line;
        while (std::getline(jsonl, line)) {
            lines.push_back(line + "\n");
        }
        jsonl.close();

        std::vector<std::string> expected_lines = {
            "{\"Name\":\"Alice\",\"Age\":30,\"Country\":\"USA\"}\n",
            "{\"Name\":\"Bob\",\"Age\":25,\"Country\":\"Canada\"}\n"
        };

        REQUIRE(lines == expected_lines);
    }

    SECTION("Single Row TSV") {
        std::string tsv_content = "Name\tAge\tCountry\nAlice\t30\tUSA\n";
        std::string tsv_file = (temp_dir / "test_single_row.tsv").string();
        std::string jsonl_file = (temp_dir / "test_single_row.jsonl").string();

        std::ofstream tsv(tsv_file);
        tsv << tsv_content;
        tsv.close();

        tsv_to_jsonl(tsv_file, jsonl_file);

        std::ifstream jsonl(jsonl_file);
        std::vector<std::string> lines;
        std::string line;
        while (std::getline(jsonl, line)) {
            lines.push_back(line + "\n");
        }
        jsonl.close();

        std::vector<std::string> expected_lines = {
            "{\"Name\":\"Alice\",\"Age\":30,\"Country\":\"USA\"}\n"
        };

        REQUIRE(lines == expected_lines);
    }

    SECTION("Numeric and Boolean Values") {
        std::string tsv_content = "Name\tAge\tIs_Student\nAlice\t30\tTrue\nBob\t25\tFalse\n";
        std::string tsv_file = (temp_dir / "test_numeric_boolean.tsv").string();
        std::string jsonl_file = (temp_dir / "test_numeric_boolean.jsonl").string();

        std::ofstream tsv(tsv_file);
        tsv << tsv_content;
        tsv.close();

        tsv_to_jsonl(tsv_file, jsonl_file);

        std::ifstream jsonl(jsonl_file);
        std::vector<std::string> lines;
        std::string line;
        while (std::getline(jsonl, line)) {
            lines.push_back(line + "\n");
        }
        jsonl.close();

        std::vector<std::string> expected_lines = {
            "{\"Name\":\"Alice\",\"Age\":30,\"Is_Student\":true}\n",
            "{\"Name\":\"Bob\",\"Age\":25,\"Is_Student\":false}\n"
        };

        REQUIRE(lines == expected_lines);
    }

    // Clean up the temporary directory
    fs::remove_all(temp_dir);
}