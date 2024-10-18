const re = require('re');

function prepareQuery(sql, params) {
    /**
     * This function modifies a SQL query string containing named parameters
     * (like $name, $age) into a format compatible with libraries that require
     * positional parameters (like $1, $2, etc.), such as asyncpg. It returns
     * a tuple containing the modified SQL string and a list of parameter values
     * ordered according to their new positions in the query.
     *
     * @param {string} sql - The original SQL query string with named parameters.
     * @param {Object} params - A dictionary mapping parameter names to their values.
     * @returns {Array} - An array where the first element is the modified SQL query string
     *                    with positional parameters, and the second element is a list of
     *                    parameter values sorted according to the order of the positional parameters.
     */

    // Find all occurrences of named parameters in the SQL string
    const namedParams = sql.match(/\$(\w+)/g).map(match => match.slice(1));

    // Remove duplicates while preserving order
    const uniqueParams = [...new Set(namedParams)];

    // Substitute each named parameter with its corresponding positional parameter
    uniqueParams.forEach((param, index) => {
        sql = sql.replace(new RegExp(`\\$${param}`, 'g'), `$${index + 1}`);
    });

    // Prepare the list of values corresponding to the order of the positional parameters
    const values = uniqueParams.filter(param => param in params).map(param => params[param]);

    return [sql, values];
}
