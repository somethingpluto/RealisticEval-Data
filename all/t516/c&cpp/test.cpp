#include <catch2/catch_test_macros.hpp>
#include <fstream>
#include <yaml-cpp/yaml.h>
#include <filesystem>

namespace fs = std::filesystem;

TEST_CASE("TestReadYaml", "[YAML]") {
    const std::string valid_yaml_file = "test_valid.yaml";
    const std::string invalid_yaml_file = "test_invalid.yaml";
    const std::string non_existent_file = "non_existent.yaml";
    const std::string empty_yaml_file = "test_empty.yaml";

    SECTION("setUp") {
        // Valid YAML content
        std::ofstream valid_file(valid_yaml_file);
        valid_file << "name: Example\nversion: 1.0\ndependencies:\n  - package1\n  - package2\n";
        valid_file.close();

        // Invalid YAML content
        std::ofstream invalid_file(invalid_yaml_file);
        invalid_file << "name: Example\nversion: 1.0\ndependencies:\n  - package1\n  - package2\ninvalid_yaml: \n - ";
        invalid_file.close();
    }

    SECTION("tearDown") {
        if (fs::exists(valid_yaml_file)) {
            fs::remove(valid_yaml_file);
        }
        if (fs::exists(invalid_yaml_file)) {
            fs::remove(invalid_yaml_file);
        }
        if (fs::exists(empty_yaml_file)) {
            fs::remove(empty_yaml_file);
        }
    }

    SECTION("test_read_valid_yaml") {
        // Test reading a valid YAML file
        YAML::Node expected_data = YAML::Load(
            "name: Example\n"
            "version: 1.0\n"
            "dependencies:\n"
            "  - package1\n"
            "  - package2\n"
        );

        YAML::Node result = read_yaml(valid_yaml_file);
        REQUIRE(result == expected_data);
    }

    SECTION("test_file_not_found") {
        // Test for FileNotFoundError when the file does not exist
        REQUIRE_THROWS_AS(read_yaml(non_existent_file), std::runtime_error);
    }

    SECTION("test_empty_yaml_file") {
        // Test reading an empty YAML file
        std::ofstream empty_file(empty_yaml_file);
        empty_file << "";  // Create an empty YAML file
        empty_file.close();

        YAML::Node result = read_yaml(empty_yaml_file);
        REQUIRE(result.IsNull());  // Expecting an empty node for an empty file
    }
}