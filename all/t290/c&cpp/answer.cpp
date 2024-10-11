#include <iostream>
#include <string>
#include <map>
#include <Poco/JSON/Object.h>
#include <Poco/JSON/Parser.h>

namespace Poco {
    namespace JSON {
        class Object;
    }
}

std::map<std::string, std::string> rdf_jsonld_to_ngsild(const std::string& rdf_jsonld) {
    // Parse the RDF JSON-LD string into a POCO JSON object
    Poco::JSON::Parser parser;
    auto json = parser.parse(rdf_jsonld).extract<Poco::JSON::Object::Ptr>();

    // Create an empty map to store the NGSI-LD output
    std::map<std::string, std::string> ngsi_ld;

    // Iterate through the keys in the JSON object
    for (auto it = json->begin(); it != json->end(); ++it) {
        const std::string& key = it->first;
        const Poco::Dynamic::Var& value = it->second;

        if (value.type() == typeid(std::string)) {
            ngsi_ld[key] = value.convert<std::string>();
        } else if (value.type() == typeid(Poco::JSON::Array)) {
            // Handle arrays if needed
            // For simplicity, we'll just convert each element to a string
            std::ostringstream oss;
            Poco::JSON::Array array = value.extract<Poco::JSON::Array>();
            for (const auto& elem : array) {
                if (elem.type() == typeid(std::string)) {
                    oss << elem.convert<std::string>() << ", ";
                }
            }
            ngsi_ld[key] = oss.str();
        }
        // Add more conditions for other types if necessary
    }

    return ngsi_ld;
}
