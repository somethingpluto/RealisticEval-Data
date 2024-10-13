TEST_CASE("Test XML to DataFrame conversion", "[xml_to_dataframe]") {
    SECTION("Single sequence") {
        const std::string xml_data = R"(<root>
                                            <sequence>
                                                <name>John</name>
                                                <age>30</age>
                                            </sequence>
                                        </root>)";
        auto result = xml_to_vector_of_maps(xml_data);
        REQUIRE(result.size() == 1);
        REQUIRE(result[0]["name"] == "John");
        REQUIRE(result[0]["age"] == "30");
    }

    SECTION("Multiple sequences") {
        const std::string xml_data = R"(<root>
                                            <sequence>
                                                <name>Alice</name>
                                                <age>25</age>
                                            </sequence>
                                            <sequence>
                                                <name>Bob</name>
                                                <age>22</age>
                                            </sequence>
                                        </root>)";
        auto result = xml_to_vector_of_maps(xml_data);
        REQUIRE(result.size() == 2);
        REQUIRE(result[0]["name"] == "Alice");
        REQUIRE(result[0]["age"] == "25");
        REQUIRE(result[1]["name"] == "Bob");
        REQUIRE(result[1]["age"] == "22");
    }

    SECTION("Empty sequence") {
        const std::string xml_data = R"(<root>
                                            <sequence></sequence>
                                        </root>)";
        auto result = xml_to_vector_of_maps(xml_data);
        REQUIRE(result.size() == 1);
        REQUIRE(result[0].empty());
    }

    SECTION("Mixed content") {
        const std::string xml_data = R"(<root>
                                            <sequence>
                                                <name>Chris</name>
                                            </sequence>
                                            <sequence>
                                                <age>28</age>
                                            </sequence>
                                        </root>)";
        auto result = xml_to_vector_of_maps(xml_data);
        REQUIRE(result.size() == 2);
        REQUIRE(result[0]["name"] == "Chris");
        REQUIRE(!result[0].count("age"));
        REQUIRE(!result[1].count("name"));
        REQUIRE(result[1]["age"] == "28");
    }

    SECTION("No sequences") {
        const std::string xml_data = R"(<root></root>)";
        auto result = xml_to_vector_of_maps(xml_data);
        REQUIRE(result.empty());
    }
}