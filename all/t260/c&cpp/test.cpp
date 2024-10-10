TEST_CASE("Process CSV with no empty columns", "[processCSV]") {
    std::string input_csv = "col1,col2,col3\n"
                             "data1,data2,data3\n"
                             "data4,data5,data6";

    std::string temp_input_file = createTempCsvFile(input_csv);
    std::string temp_output_file = "output.csv";

    processCSV(temp_input_file, temp_output_file);

    std::string expected_output = "col1,col2,col3\n"
                                  "data1,data2,data3\n"
                                  "data4,data5,data6";

    REQUIRE(readCsvFile(temp_output_file) == expected_output);
}

TEST_CASE("Process CSV with one empty column", "[processCSV]") {
    std::string input_csv = "col1,col2,col3\n"
                             "data1,,data3\n"
                             "data4,data5,data6";

    std::string temp_input_file = createTempCsvFile(input_csv);
    std::string temp_output_file = "output.csv";

    processCSV(temp_input_file, temp_output_file);

    std::string expected_output = "col1,col2,col3\n"
                                  "data1,,data3\n"
                                  "data4,data5,data6";

    REQUIRE(readCsvFile(temp_output_file) == expected_output);
}

TEST_CASE("Process CSV with two consecutive empty columns", "[processCSV]") {
    std::string input_csv = "col1,col2,col3\n"
                             "data1,,\n"
                             "data4,data5,data6";

    std::string temp_input_file = createTempCsvFile(input_csv);
    std::string temp_output_file = "output.csv";

    processCSV(temp_input_file, temp_output_file);

    std::string expected_output = "col1,col2,col3\n"
                                  "data4,data5,data6";

    REQUIRE(readCsvFile(temp_output_file) == expected_output);
}

TEST_CASE("Process CSV with all empty columns", "[processCSV]") {
    std::string input_csv = "col1,col2,col3\n"
                             ",,\n"
                             ",,\n";

    std::string temp_input_file = createTempCsvFile(input_csv);
    std::string temp_output_file = "output.csv";

    processCSV(temp_input_file, temp_output_file);

    std::string expected_output = "";

    REQUIRE(readCsvFile(temp_output_file) == expected_output);
}

TEST_CASE("Process empty CSV file", "[processCSV]") {
    std::string input_csv = "";

    std::string temp_input_file = createTempCsvFile(input_csv);
    std::string temp_output_file = "output.csv";

    processCSV(temp_input_file, temp_output_file);

    std::string expected_output = "";

    REQUIRE(readCsvFile(temp_output_file) == expected_output);
}