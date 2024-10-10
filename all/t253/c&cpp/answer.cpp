#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

void log(const std::string& item) {
    std::cout << "String: " << item << std::endl;
}

void log(int item) {
    std::cout << "Number: " << item << std::endl;
}

void log(double item) {
    std::cout << "Number: " << item << std::endl;
}

template<typename T>
void log(const std::vector<T>& item) {
    std::cout << "List: [";
    for (size_t i = 0; i < item.size(); ++i) {
        if (i > 0) std::cout << ", ";
        log(item[i]);
    }
    std::cout << "]" << std::endl;
}

template<typename Key, typename Value>
void log(const std::map<Key, Value>& item) {
    std::cout << "Dictionary: {";
    size_t count = 0;
    for (const auto& pair : item) {
        if (count > 0) std::cout << ", ";
        std::cout << "\"" << pair.first << "\": ";
        log(pair.second);
        ++count;
    }
    std::cout << "}" << std::endl;
}

void log(const json& item) {
    std::cout << "JSON: " << item.dump(4) << std::endl;
}

template<typename T>
T log(T item) {
    // Handle other types by reporting as errors
    std::cerr << "Error: Unsupported type" << std::endl;
    return item;
}