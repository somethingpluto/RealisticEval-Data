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