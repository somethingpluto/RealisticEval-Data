function prepareQuery(sql, params) {
    /**
     * This function modifies a SQL query string containing named parameters
     * (like $name, $age) into a format compatible with libraries that require
     * positional parameters (like $1, $2, etc.), such as asyncpg. It returns
     * a tuple containing the modified SQL string and a list of parameter values
     * ordered according to their new positions in the query.
     *
     * Example:
     *   Input:
     *     sql: "SELECT * FROM users WHERE id = $user_id AND status = $status"
     *     params: {'user_id': 42, 'status': 'active'}
     *   Output:
     *     ["SELECT * FROM users WHERE id = $1 AND status = $2", [42, 'active']]
     *
     * @param {string} sql - The original SQL query string with named parameters.
     * @param {Object} params - A dictionary mapping parameter names to their values.
     * @returns {Array} - An array where the first element is the modified SQL query string
     *                    with positional parameters, and the second element is a list of
     *                    parameter values sorted according to the order of the positional parameters.
     */
}