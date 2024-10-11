#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>

// Define a simple structure to hold parameter information
struct ParameterInfo {
    std::string name;
    std::string type; // Simplified type representation
};

// Function to get parameter information from a function pointer
std::vector<ParameterInfo> getFunctionParameters(void (*func)()) {
    // This is a placeholder implementation. In practice, you would need to use
    // a library like Boost.Python or SWIG to extract function signatures at runtime.
    std::vector<ParameterInfo> params;
    params.push_back({"param1", "int"});
    params.push_back({"param2", "double"});
    return params;
}

// Main function to check method argument types
void method_arg_type_check(void (*method)(int, double), int arg1, double arg2) {
    auto params = getFunctionParameters(method);

    // Check positional arguments
    if (params.size() > 0 && typeid(arg1).name() != params[0].type) {
        throw std::invalid_argument("Type mismatch in argument 'param1'");
    }
    if (params.size() > 1 && typeid(arg2).name() != params[1].type) {
        throw std::invalid_argument("Type mismatch in argument 'param2'");
    }

    std::cout << "All arguments match!" << std::endl;
}