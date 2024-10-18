import { replace, match } from 'lodash';

function prepareQuery(sql: string, params: Record<string, any>): [string, any[]] {
    /**
     * This function modifies a SQL query string containing named parameters
     * (like $name, $age) into a format compatible with libraries that require
     * positional parameters (like $1, $2, etc.), such as asyncpg. It returns
     * a tuple containing the modified SQL string and a list of parameter values
     * ordered according to their new positions in the query.
     *
     * @param sql - The original SQL query string with named parameters.
     * @param params - A dictionary mapping parameter names to their values.
     * @returns A tuple where the first element is the modified SQL query string
     *          with positional parameters, and the second element is a list of
     *          parameter values sorted according to the order of the positional parameters.
     */

    // Find all occurrences of named parameters in the SQL string
    const namedParams = match(sql, /\$(\w+)/g);

    // Remove duplicates while preserving order
    const uniqueParams = Array.from(new Set(namedParams));

    // Substitute each named parameter with its corresponding positional parameter
    let modifiedSql = sql;
    for (let index = 0; index < uniqueParams.length; index++) {
        const param = uniqueParams[index];
        const paramName = param.substring(1); // Extract the name without the '$'
        modifiedSql = modifiedSql.replace(new RegExp(`\\$${paramName}`, 'g'), `$${index + 1}`);
    }

    // Prepare the list of values corresponding to the order of the positional parameters
    const values = uniqueParams.map(param => {
        const paramName = param.substring(1); // Extract the name without the '$'
        return params[paramName];
    }).filter(value => value !== undefined);

    return [modifiedSql, values];
}