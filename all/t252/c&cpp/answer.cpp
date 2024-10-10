#include <iostream>
#include <string>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class BitSequenceEncoder : public json::serializer<json> {
public:
    static void encode(json &j, const std::string &key, const json &value) {
        if (key == "bits" && value.is_number_integer()) {
            j[key] = std::bitset<32>(value.get<int>()).to_string();
        } else {
            j[key] = value;
        }
    }

    template<typename T>
    static void encode(json &j, const std::string &key, const T &value) {
        json::serializer<json>::encode(j, key, value);
    }
};