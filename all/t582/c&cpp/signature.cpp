/**
 * Converts an object to a query string.
 * For example:
 *      input: { "search": "test", "page": "1", "size": "10" };
 *      output: ?search=test&page=1&size=10
 *
 * @param params - The parameters to convert.
 * @returns The query string.
 */
std::string toQueryString(const std::map<std::string, std::string>& params){}