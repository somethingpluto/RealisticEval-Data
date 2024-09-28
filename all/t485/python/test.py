import unittest


# Assuming the prepare_query function is defined above or imported

class TestPrepareQuery(unittest.TestCase):

    def test_valid_named_parameters(self):
        sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $status"
        parameters = {
            'user_id': 42,
            'status': 'active'
        }
        expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $2"
        expected_values = [42, 'active']

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)

    def test_missing_parameters(self):
        sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $status"
        parameters = {
            'user_id': 42  # 'status' is missing
        }
        expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $2"
        expected_values = [42]  # 'status' is not included

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)

    def test_no_parameters(self):
        sql_query = "SELECT * FROM users"
        parameters = {}  # No parameters provided
        expected_sql = "SELECT * FROM users"
        expected_values = []

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)

    def test_multiple_same_parameters(self):
        sql_query = "SELECT * FROM users WHERE id = $user_id AND status = $user_id"
        parameters = {
            'user_id': 42
        }
        expected_sql = "SELECT * FROM users WHERE id = $1 AND status = $1"
        expected_values = [42]  # Only one value for 'user_id'

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)

    def test_special_characters_in_parameters(self):
        sql_query = "INSERT INTO users (name, email) VALUES ($name, $email)"
        parameters = {
            'name': "John Doe",
            'email': "john.doe@example.com"
        }
        expected_sql = "INSERT INTO users (name, email) VALUES ($1, $2)"
        expected_values = ["John Doe", "john.doe@example.com"]

        new_sql, value_list = prepare_query(sql_query, parameters)
        self.assertEqual(new_sql, expected_sql)
        self.assertEqual(value_list, expected_values)