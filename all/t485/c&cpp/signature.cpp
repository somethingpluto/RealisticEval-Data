/**
 * This function modifies a SQL query string containing named parameters
 * (like $name, $age) into a format compatible with libraries that require
 * positional parameters (like $1, $2, etc.), such as asyncpg. It returns
 * a pair containing the modified SQL string and a vector of parameter values
 * ordered according to their new positions in the query.
 * 
 * Example:
 *     Input:
 *         sql: SELECT * FROM users WHERE id = $user_id AND status = $status
 *         params: {{"user_id", "42"}, {"status", "active"}}
 *     Output:
 *         Modified SQL: SELECT * FROM users WHERE id = $1 AND status = $2
 *         Values: ["42", "active"]
 * 
 * @param sql The original SQL query string with named parameters.
 * @param params A map mapping parameter names to their values.
 * @return A pair where the first element is the modified SQL query string with positional parameters,
 *         and the second element is a vector of parameter values sorted according to the order of the positional parameters.
 */
std::pair<std::string, std::vector<std::string>> prepare_query(const std::string& sql, const std::map<std::string, std::string>& params) {}