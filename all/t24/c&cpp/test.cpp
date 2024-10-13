TEST_CASE("Test conversion of YAML files to JSON") {
    // Create temporary YAML files for testing
    const std::string simple_yaml = "simple.yaml";
    const std::string nested_yaml = "nested.yaml";
    const std::string empty_yaml = "empty.yaml";
    const std::string list_yaml = "list.yaml";
    const std::string invalid_yaml = "invalid.yaml";

    SECTION("Setup temporary files") {
        // Write simple YAML file
        std::ofstream simpleFile(simple_yaml);
        simpleFile << "name: John Doe\nage: 30\n";
        simpleFile.close();

        // Write nested YAML file
        std::ofstream nestedFile(nested_yaml);
        nestedFile << "person:\n  name: Jane Doe\n  age: 25\n  address:\n    city: New York\n    zip: 10001\n";
        nestedFile.close();

        // Write empty YAML file
        std::ofstream emptyFile(empty_yaml);
        emptyFile.close();

        // Write list YAML file
        std::ofstream listFile(list_yaml);
        listFile << "- item1\n- item2\n- item3\n";
        listFile.close();

        // Write invalid YAML file
        std::ofstream invalidFile(invalid_yaml);
        invalidFile << "{ invalid: YAML: structure }\n";
        invalidFile.close();
    }

    SECTION("Test simple YAML conversion") {
        convertYamlToJson(simple_yaml, "output.json");
        std::ifstream jsonFile("output.json");
        REQUIRE(jsonFile.is_open());
        json jsonData;
        jsonFile >> jsonData;
        REQUIRE(jsonData == (json{{"name", "John Doe"}, {"age", 30}}));
    }

    SECTION("Test nested YAML conversion") {
        convertYamlToJson(nested_yaml, "output.json");
        std::ifstream jsonFile("output.json");
        REQUIRE(jsonFile.is_open());
        json jsonData;
        jsonFile >> jsonData;
        REQUIRE(jsonData == (json{
            {"person", {
                {"name", "Jane Doe"},
                {"age", 25},
                {"address", {
                    {"city", "New York"},
                    {"zip", 10001}
                }}
            }}
        }));
    }

    SECTION("Test empty YAML conversion") {
        convertYamlToJson(empty_yaml, "output.json");
        std::ifstream jsonFile("output.json");
        REQUIRE(jsonFile.is_open());
        json jsonData;
        jsonFile >> jsonData;
        REQUIRE(jsonData.is_null());
    }

    SECTION("Test list YAML conversion") {
        convertYamlToJson(list_yaml, "output.json");
        std::ifstream jsonFile("output.json");
        REQUIRE(jsonFile.is_open());
        json jsonData;
        jsonFile >> jsonData;
        REQUIRE(jsonData == (json{"item1", "item2", "item3"}));
    }

    SECTION("Test invalid YAML conversion") {
        REQUIRE_THROWS_AS(convertYamlToJson(invalid_yaml, "output.json"), YAML::Exception);
    }

    SECTION("Teardown temporary files") {
        std::remove(simple_yaml.c_str());
        std::remove(nested_yaml.c_str());
        std::remove(empty_yaml.c_str());
        std::remove(list_yaml.c_str());
        std::remove(invalid_yaml.c_str());
        if (std::ifstream("output.json").is_open()) {
            std::remove("output.json");
        }
    }
}