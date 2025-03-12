import re

def prepare_query(sql: str, params: dict) -> tuple:
    """
    This function modifies a SQL query string containing named parameters
    (like $name, $age) into a format compatible with libraries that require
    positional parameters (like $1, $2, etc.), such as asyncpg. It returns
    a tuple containing the modified SQL string and a list of parameter values
    ordered according to their new positions in the query.
    For example:
        input:
            sql: SELECT * FROM users WHERE id = $user_id AND status = $status
            params: {'user_id': 42,'status': 'active'}
        output:
            SELECT * FROM users WHERE id = $1 AND status = $2,[42, 'active']

    Args:
        sql (str): The original SQL query string with named parameters.
        params (dict): A dictionary mapping parameter names to their values.

    Returns:
        tuple: A tuple where the first element is the modified SQL query string with positional parameters, and the second element is a list of parameter values sorted according to the order of the positional parameters.
    """
    param_names = sorted(params.keys())
    param_values = [params[name] for name in param_names]
    param_positions = {name: f'${i+1}' for i, name in enumerate(param_names)}

    def replace_param(match):
        param_name = match.group(1)
        return param_positions[param_name]

    modified_sql = re.sub(r'\$(\w+)', replace_param, sql)
    return modified_sql, param_values
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
if __name__ == '__main__':
    unittest.main()