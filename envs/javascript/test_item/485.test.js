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
function prepareQuery(sql, params) {
    let paramPositions = {};
    let paramValues = [];
    let modifiedSql = sql.replace(/\$(\w+)/g, (match, paramName) => {
        if (!paramPositions[paramName]) {
            paramPositions[paramName] = paramValues.length + 1;
            paramValues.push(params[paramName]);
        }
        return `$${paramPositions[paramName]}`;
    });
    return [modifiedSql, paramValues];
}
describe('TestPrepareQuery', () => {
    it('test_valid_named_parameters', () => {
        const sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $status";
        const parameters = {
            'user_id': 42,
            'status': 'active'
        };
        const expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $2";
        const expected_values = [42, 'active'];

        const [new_sql, value_list] = prepareQuery(sql_query, parameters);
        expect(new_sql).toEqual(expected_sql);
        expect(value_list).toEqual(expected_values);
    });

    it('test_missing_parameters', () => {
        const sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $status";
        const parameters = {
            'user_id': 42  // 'status' is missing
        };
        const expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $2";
        const expected_values = [42];  // 'status' is not included

        const [new_sql, value_list] = prepareQuery(sql_query, parameters);
        expect(new_sql).toEqual(expected_sql);
        expect(value_list).toEqual(expected_values);
    });

    it('test_no_parameters', () => {
        const sql_query = "SELECT * FROM users";
        const parameters = {};  // No parameters provided
        const expected_sql = "SELECT * FROM users";
        const expected_values = [];

        const [new_sql, value_list] = prepareQuery(sql_query, parameters);
        expect(new_sql).toEqual(expected_sql);
        expect(value_list).toEqual(expected_values);
    });

    it('test_multiple_same_parameters', () => {
        const sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $user_id";
        const parameters = {
            'user_id': 42
        };
        const expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $1";
        const expected_values = [42];  // Only one value for 'user_id'

        const [new_sql, value_list] = prepareQuery(sql_query, parameters);
        expect(new_sql).toEqual(expected_sql);
        expect(value_list).toEqual(expected_values);
    });

    it('test_special_characters_in_parameters', () => {
        const sql_query = "INSERT INTO users (name, email) VALUES ($name, $email)";
        const parameters = {
            'name': "John Doe",
            'email': "john.doe@example.com"
        };
        const expected_sql = "INSERT INTO users (name, email) VALUES ($1, $2)";
        const expected_values = ["John Doe", "john.doe@example.com"];

        const [new_sql, value_list] = prepareQuery(sql_query, parameters);
        expect(new_sql).toEqual(expected_sql);
        expect(value_list).toEqual(expected_values);
    });
});
