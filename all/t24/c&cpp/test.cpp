#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() automatically
#include <catch2/catch.hpp>
#include <fstream>
#include <cstdio>
#include "yaml-cpp/yaml.h"
#include "nlohmann/json.hpp"

void convertYamlToJson(const std::string& yamlFile, const std::string& jsonFile);

TEST_CASE("Test YAML to JSON Conversion") {
    std::string output_json = "output.json";

    auto setupFile = [](const std::string& filename, const std::string& content) {
        std::ofstream file(filename);
        REQUIRE(file.is_open());
        file << content;
        file.close();
    };

    auto teardownFile = [](const std::string& filename) {
        std::remove(filename.c_str());
    };

    SECTION("Simple YAML Conversion") {
        std::string simple_yaml = "simple.yaml";
        setupFile(simple_yaml, "name: John Doe\nage: 30\n");

        convertYamlToJson(simple_yaml, output_json);

        std::ifstream jf(output_json);
        REQUIRE(jf.is_open());
        nlohmann::json data;
        jf >> data;
        jf.close();

        nlohmann::json expected = {{"name", "John Doe"}, {"age", 30}};
        REQUIRE(data == expected);

        teardownFile(simple_yaml);
    }

    SECTION("Nested YAML Conversion") {
        std::string nested_yaml = "nested.yaml";
        setupFile(nested_yaml, "person:\n  name: Jane Doe\n  age: 25\n  address:\n    city: New York\n    zip: 10001\n");

        convertYamlToJson(nested_yaml, output_json);

        std::ifstream jf(output_json);
        REQUIRE(jf.is_open());
        nlohmann::json data;
        jf >> data;
        jf.close();

        nlohmann::json expected = {
            {"person", {
                {"name", "Jane Doe"},
                {"age", 25},
                {"address", {
                    {"city", "New York"},
                    {"zip", 10001}
                }}
            }}
        };
        REQUIRE(data == expected);

        teardownFile(nested_yaml);
    }

    SECTION("Empty YAML Conversion") {
        std::string empty_yaml = "empty.yaml";
        setupFile(empty_yaml, "");

        convertYamlToJson(empty_yaml, output_json);

        std::ifstream jf(output_json);
        REQUIRE(jf.is_open());
        nlohmann::json data;
        jf >> data;
        jf.close();

        REQUIRE(data.is_null());

        teardownFile(empty_yaml);
    }

    SECTION("List YAML Conversion") {
        std::string list_yaml = "list.yaml";
        setupFile(list_yaml, "- item1\n- item2\n- item3\n");

        convertYamlToJson(list_yaml, output_json);

        std::ifstream jf(output_json);
        REQUIRE(jf.is_open());
        nlohmann::json data;
        jf >> data;
        jf.close();

        nlohmann::json expected = {"item1", "item2", "item3"};
        REQUIRE(data == expected);

        teardownFile(list_yaml);
    }

    SECTION("Invalid YAML Conversion") {
        std::string invalid_yaml = "invalid.yaml";
        setupFile(invalid_yaml, "{ invalid: YAML: structure }\n");

        REQUIRE_THROWS_AS(
            convertYamlToJson(invalid_yaml, output_json),
            YAML::ParserException
        );

        teardownFile(invalid_yaml);
    }

    // Clean up
    teardownFile(output_json);
}