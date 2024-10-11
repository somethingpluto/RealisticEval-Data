TEST_CASE("Test RDF to NGSI-LD Conversion") {
    std::string input_data = R"({
        "@context": {"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "@vocab": "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core#"},
        "@id": "urn:ngsi-ld:Example:001",
        "type": "ExampleType",
        "exampleProperty": "exampleValue"
    })";

    nlohmann::json expected_output = {
        { "id", "urn:ngsi-ld:Example:001" },
        { "type", "ExampleType" },
        { "exampleProperty", "exampleValue" }
    };

    auto output = rdf_jsonld_to_ngsild(input_data);

    REQUIRE(output == expected_output);
}