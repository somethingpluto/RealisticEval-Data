#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <regex>

// Function to prepare the SQL query and parameter values
std::pair<std::string, std::vector<std::string>> prepare_query(const std::string& sql, const std::map<std::string, std::string>& params) {
    /**
     * This function modifies a SQL query string containing named parameters
     * (like $name, $age) into a format compatible with libraries that require
     * positional parameters (like $1, $2, etc.), such as asyncpg. It returns
     * a pair containing the modified SQL string and a vector of parameter values
     * ordered according to their new positions in the query.
     *
     * Args:
     *     sql (const std::string&): The original SQL query string with named parameters.
     *     params (const std::map<std::string, std::string>&): A map mapping parameter names to their values.
     *
     * Returns:
     *     std::pair<std::string, std::vector<std::string>>: A pair where the first element is the modified SQL query string
     *                                                       with positional parameters, and the second element is a vector of
     *                                                       parameter values sorted according to the order of the positional parameters.
     */

    // Find all occurrences of named parameters in the SQL string
    std::regex named_param_pattern("\\$([a-zA-Z][a-zA-Z0-9]*)");
    std::sregex_iterator it(sql.begin(), sql.end(), named_param_pattern);
    std::sregex_iterator end;

    std::vector<std::string> named_params;
    for (; it != end; ++it) {
        named_params.push_back(it->str());
    }

    // Remove duplicates while preserving order
    std::map<std::string, bool> seen;
    std::vector<std::string> unique_params;
    for (const auto& param : named_params) {
        std::string paramName = param.substr(1); // Remove the '$' prefix
        if (seen.find(paramName) == seen.end()) {
            seen[paramName] = true;
            unique_params.push_back(param);
        }
    }

    // Substitute each named parameter with its corresponding positional parameter
    for (size_t index = 1; index <= unique_params.size(); ++index) {
        std::string param = unique_params[index - 1];
        std::string paramName = param.substr(1); // Remove the '$' prefix
        std::string replacement = "$" + std::to_string(index);
        sql = std::regex_replace(sql, std::regex("\\$" + paramName), replacement);
    }

    // Prepare the list of values corresponding to the order of the positional parameters
    std::vector<std::string> values;
    for (const auto& param : unique_params) {
        std::string paramName = param.substr(1); // Remove the '$' prefix
        auto it = params.find(paramName);
        if (it != params.end()) {
            values.push_back(it->second);
        }
    }

    return {sql, values};
}
