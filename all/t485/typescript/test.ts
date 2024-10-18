describe('TestPrepareQuery', () => {
    it('test valid named parameters', () => {
        const sqlQuery = "SELECT * FROM users WHERE id = $user_id AND status = $status";
        const parameters = {
            user_id: 42,
            status: 'active'
        };
        const expectedSql = "SELECT * FROM users WHERE id = $1 AND status = $2";
        const expectedValues = [42, 'active'];

        const [newSql, valueList] = prepareQuery(sqlQuery, parameters);
        expect(newSql).toEqual(expectedSql);
        expect(valueList).toEqual(expectedValues);
    });

    it('test missing parameters', () => {
        const sqlQuery = "SELECT * FROM users WHERE id = $user_id AND status = $status";
        const parameters = {
            user_id: 42  // 'status' is missing
        };
        const expectedSql = "SELECT * FROM users WHERE id = $1 AND status = $2";
        const expectedValues = [42];  // 'status' is not included

        const [newSql, valueList] = prepareQuery(sqlQuery, parameters);
        expect(newSql).toEqual(expectedSql);
        expect(valueList).toEqual(expectedValues);
    });

    it('test no parameters', () => {
        const sqlQuery = "SELECT * FROM users";
        const parameters = {};  // No parameters provided
        const expectedSql = "SELECT * FROM users";
        const expectedValues = [];

        const [newSql, valueList] = prepareQuery(sqlQuery, parameters);
        expect(newSql).toEqual(expectedSql);
        expect(valueList).toEqual(expectedValues);
    });

    it('test multiple same parameters', () => {
        const sqlQuery = "SELECT * FROM users WHERE id = $user_id AND status = $user_id";
        const parameters = {
            user_id: 42
        };
        const expectedSql = "SELECT * FROM users WHERE id = $1 AND status = $1";
        const expectedValues = [42];  // Only one value for 'user_id'

        const [newSql, valueList] = prepareQuery(sqlQuery, parameters);
        expect(newSql).toEqual(expectedSql);
        expect(valueList).toEqual(expectedValues);
    });

    it('test special characters in parameters', () => {
        const sqlQuery = "INSERT INTO users (name, email) VALUES ($name, $email)";
        const parameters = {
            name: "John Doe",
            email: "john.doe@example.com"
        };
        const expectedSql = "INSERT INTO users (name, email) VALUES ($1, $2)";
        const expectedValues = ["John Doe", "john.doe@example.com"];

        const [newSql, valueList] = prepareQuery(sqlQuery, parameters);
        expect(newSql).toEqual(expectedSql);
        expect(valueList).toEqual(expectedValues);
    });
});