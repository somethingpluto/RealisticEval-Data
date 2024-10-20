TEST_CASE("TestProcessCSV", "[process_csv]") {
    SECTION("Test Case 1") {
        const std::string input_data_1 = R"(
A,B,C
1,2,3
4,,6
7,8,
9,10,11
)";

        const std::string input_file_path = "input.csv";
        const std::string output_file_path = "output.csv";

        // Write input data to a temp CSV file
        std::ofstream input_file(input_file_path);
        input_file << input_data_1;
        input_file.close();

        // Process the CSV
        process_csv(input_file_path, output_file_path);

        // Read the output
        std::ifstream output_file(output_file_path);
        std::stringstream output_stream;
        output_stream << output_file.rdbuf();
        std::string output_data = output_stream.str();
        output_file.close();

        // Clean up temp files
        fs::remove(input_file_path);
        fs::remove(output_file_path);

        const std::string expected_output = R"(
A,B,C
1,2.0,3.0
4,,6.0
7,8.0,
9,10.0,11.0
)";

        REQUIRE(output_data == expected_output);
    }

    SECTION("Test Case 2") {
        const std::string input_data_2 = R"(
A,B,C,D
,,
1,,3,4
2,3,,5
,,,
)";

        const std::string input_file_path = "input.csv";
        const std::string output_file_path = "output.csv";

        // Write input data to a temp CSV file
        std::ofstream input_file(input_file_path);
        input_file << input_data_2;
        input_file.close();

        // Process the CSV
        process_csv(input_file_path, output_file_path);

        // Read the output
        std::ifstream output_file(output_file_path);
        std::stringstream output_stream;
        output_stream << output_file.rdbuf();
        std::string output_data = output_stream.str();
        output_file.close();

        // Clean up temp files
        fs::remove(input_file_path);
        fs::remove(output_file_path);

        const std::string expected_output = R"(
A,B,C,D
1.0,,3.0,4.0
2.0,3.0,,5.0
)";

        REQUIRE(output_data == expected_output);
    }

    SECTION("Test Case 3") {
        const std::string input_data_3 = R"(
A
1
2
3
)";

        const std::string input_file_path = "input.csv";
        const std::string output_file_path = "output.csv";

        // Write input data to a temp CSV file
        std::ofstream input_file(input_file_path);
        input_file << input_data_3;
        input_file.close();

        // Process the CSV
        process_csv(input_file_path, output_file_path);

        // Read the output
        std::ifstream output_file(output_file_path);
        std::stringstream output_stream;
        output_stream << output_file.rdbuf();
        std::string output_data = output_stream.str();
        output_file.close();

        // Clean up temp files
        fs::remove(input_file_path);
        fs::remove(output_file_path);

        const std::string expected_output = R"(
A
1
2
3
)";

        REQUIRE(output_data == expected_output);
    }
}