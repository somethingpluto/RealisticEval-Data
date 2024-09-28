#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <tinyxml2.h>
#include <vector>
#include <map>
#include <string>
#include <sstream>

using namespace tinyxml2;

std::vector<std::map<std::string, std::string>> xml_to_data(const std::string& xml_file) {
    std::vector<std::map<std::string, std::string>> rows;

    XMLDocument doc;
    if (doc.LoadFile(xml_file.c_str()) != XML_SUCCESS) {
        return rows;
    }

    XMLElement* root = doc.RootElement();
    if (!root) {
        return rows;
    }

    for (XMLElement* sequence = root->FirstChildElement("sequence"); sequence != nullptr; sequence = sequence->NextSiblingElement("sequence")) {
        std::map<std::string, std::string> row_data;

        for (XMLElement* child = sequence->FirstChildElement(); child != nullptr; child = child->NextSiblingElement()) {
            row_data[child->Name()] = child->GetText() ? child->GetText() : "";
        }

        rows.push_back(row_data);
    }

    return rows;
}

TEST_CASE("Test single sequence") {
    const char* xml_data = R"(
        <root>
            <sequence>
                <name>John</name>
                <age>30</age>
            </sequence>
        </root>
    )";

    XMLDocument doc;
    doc.Parse(xml_data);
    std::stringstream ss;
    doc.SaveFile(ss);

    auto data = xml_to_data(ss.str());
    REQUIRE(data.size() == 1);
    REQUIRE(data[0]["name"] == "John");
    REQUIRE(data[0]["age"] == "30");
}

TEST_CASE("Test multiple sequences") {
    const char* xml_data = R"(
        <root>
            <sequence>
                <name>Alice</name>
                <age>25</age>
            </sequence>
            <sequence>
                <name>Bob</name>
                <age>22</age>
            </sequence>
        </root>
    )";

    XMLDocument doc;
    doc.Parse(xml_data);
    std::stringstream ss;
    doc.SaveFile(ss);

    auto data = xml_to_data(ss.str());
    REQUIRE(data.size() == 2);
    REQUIRE(data[0]["name"] == "Alice");
    REQUIRE(data[0]["age"] == "25");
    REQUIRE(data[1]["name"] == "Bob");
    REQUIRE(data[1]["age"] == "22");
}

TEST_CASE("Test empty sequence") {
    const char* xml_data = R"(
        <root>
            <sequence></sequence>
        </root>
    )";

    XMLDocument doc;
    doc.Parse(xml_data);
    std::stringstream ss;
    doc.SaveFile(ss);

    auto data = xml_to_data(ss.str());
    REQUIRE(data.size() == 1);
    REQUIRE(data[0].empty());
}

TEST_CASE("Test mixed content") {
    const char* xml_data = R"(
        <root>
            <sequence>
                <name>Chris</name>
            </sequence>
            <sequence>
                <age>28</age>
            </sequence>
        </root>
    )";

    XMLDocument doc;
    doc.Parse(xml_data);
    std::stringstream ss;
    doc.SaveFile(ss);

    auto data = xml_to_data(ss.str());
    REQUIRE(data.size() == 2);
    REQUIRE(data[0]["name"] == "Chris");
    REQUIRE(data[0]["age"].empty());
    REQUIRE(data[1]["name"].empty());
    REQUIRE(data[1]["age"] == "28");
}

TEST_CASE("Test no sequences") {
    const char* xml_data = R"(
        <root></root>
    )";

    XMLDocument doc;
    doc.Parse(xml_data);
    std::stringstream ss;
    doc.SaveFile(ss);

    auto data = xml_to_data(ss.str());
    REQUIRE(data.empty());
}