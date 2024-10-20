TEST_CASE("Test RDF JSON-LD to NGSI-LD Conversion") {
    SECTION("Basic conversion") {
        // Test a basic and correct conversion from JSON-LD to NGSI-LD
        std::string rdf_jsonld = R"({"@context": "http://schema.org/", "@id": "urn:ngsi-ld:Vehicle:A123", "@type": "Vehicle", "speed": {"value": 60, "unitCode": "KMH"}})";
        json expected_ngsild = {
            {"id", "urn:ngsi-ld:Vehicle:A123"},
            {"type", "Vehicle"},
            {"@context", "http://schema.org/"},
            {"attributes", json::array({
                {"type", "Property"},
                {"name", "speed"},
                {"value", json::object({{"value", 60}, {"unitCode", "KMH"}})}
            })}
        };
        json result = rdf_json_ld_to_ngsi_ld(rdf_jsonld);
        REQUIRE(result == expected_ngsild);
    }

    SECTION("Missing @id and @type") {
        // Test conversion when @id and @type are missing
        std::string rdf_jsonld = R"({"@context": "http://schema.org/", "speed": {"value": 60, "unitCode": "KMH"}})";
        json expected_ngsild = {
            {"id", "urn:ngsi-ld:unknown:id"},
            {"type", "UnknownType"},
            {"@context", "http://schema.org/"},
            {"attributes", json::array({
                {"type", "Property"},
                {"name", "speed"},
                {"value", json::object({{"value", 60}, {"unitCode", "KMH"}})}
            })}
        };
        json result = rdf_json_ld_to_ngsi_ld(rdf_jsonld);
        REQUIRE(result == expected_ngsild);
    }

    SECTION("With nested objects") {
        // Test conversion with nested objects
        std::string rdf_jsonld = R"({"@context": "http://schema.org/", "@id": "urn:ngsi-ld:Vehicle:A123", "@type": "Vehicle", "location": {"latitude": 48.8566, "longitude": 2.3522}})";
        json expected_ngsild = {
            {"id", "urn:ngsi-ld:Vehicle:A123"},
            {"type", "Vehicle"},
            {"@context", "http://schema.org/"},
            {"attributes", json::array({
                {"type", "Property"},
                {"name", "location"},
                {"value", json::object({{"latitude", 48.8566}, {"longitude", 2.3522}})}
            })}
        };
        json result = rdf_json_ld_to_ngsi_ld(rdf_jsonld);
        REQUIRE(result == expected_ngsild);
    }

    SECTION("Invalid JSON input") {
        // Test the function's response to invalid JSON input
        std::string rdf_jsonld = "This is not a valid JSON";
        REQUIRE_THROWS_AS(rdf_json_ld_to_ngsi_ld(rdf_jsonld), std::exception);
    }

    SECTION("Empty JSON-LD document") {
        // Test the conversion of an empty JSON-LD document
        std::string rdf_jsonld = R"({})";
        json expected_ngsild = {
            {"id", "urn:ngsi-ld:unknown:id"},
            {"type", "UnknownType"},
            {"@context", "https://schema.lab.fiware.org/ld/context"},
            {"attributes", json::array()}
        };
        json result = rdf_json_ld_to_ngsi_ld(rdf_jsonld);
        REQUIRE(result == expected_ngsild);
    }
}