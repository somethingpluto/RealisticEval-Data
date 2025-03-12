
def convert_named_to_positional_query(sql: str, params: dict) -> tuple:
    """
    This function modifies a SQL query string containing named parameters (like $name, $age) into a format compatible with libraries that require positional parameters (like $1, $2, etc.), such as asyncpg. It returns
    a tuple containing the modified SQL query string with positional parameters, and a list of parameter values sorted according to their new positions in the query.
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
python
import re

def convert_named_to_positional_query(sql: str, params: dict) -> tuple:
    # Convert named parameters to positional parameters
    sql_with_named_params = re.sub(r'[$][^]$', r'\1', sql)
    sql_with_positional_params = re.sub(r'[$][^]$', r'\1,', sql_with_named_params)

    # Convert positional parameters to named parameters
    sql_with_positional_params_with_named_params = re.sub(r'[$][^]$', r'\1', sql_with_positional_params)
    sql_with_named_params_with_named_params = re.sub(r'[$][^]$', r'\1', sql_with_named_params_with_named_params)

    # Convert named parameters to positional parameters and list parameter values
    sql_with_named_params_list = list(map(lambda x: re.sub(r'[$][^]$', r'\1', x), sql_with_named_params))
    sql_with_positional_params_list = list(map(lambda x: re.sub(r'[$][^]$', r'\1,', x), sql_with_positional_params))

    # Return modified SQL query string and list of parameter values
    return sql_with_named_params, sql_with_positional_params_list

import unittest

class TestConvertNamedToPositionalQuery(unittest.TestCase):

    def test_basic_named_parameters(self):
        sql = "SELECT * FROM users WHERE username = $username AND age = $age"
        params = {"username": "john_doe", "age": 30}
        delimiter = "$"

        expected = {
            "positional_sql": "SELECT * FROM users WHERE username = $1 AND age = $2",
            "param_list": ["john_doe", 30],
            "execute_sql": "SELECT * FROM users WHERE username = john_doe AND age = 30"
        }

        result = convert_named_to_positional_query(sql, params, delimiter)
        self.assertEqual(result, expected)

    def test_missing_parameter(self):
        sql = "SELECT * FROM products WHERE id = #product_id AND name = #product_name"
        params = {"product_id": 101}  # 'product_name' is missing
        delimiter = "#"

        with self.assertRaises(ValueError) as context:
            convert_named_to_positional_query(sql, params, delimiter)

        self.assertEqual(str(context.exception), "Parameter 'product_name' not found in params dictionary.")

    def test_different_delimiter(self):
        sql = "INSERT INTO orders (product_id, quantity) VALUES (:product_id, :quantity)"
        params = {"product_id": 202, "quantity": 5}
        delimiter = ":"

        expected = {
            "positional_sql": "INSERT INTO orders (product_id, quantity) VALUES (:1, :2)",
            "param_list": [202, 5],
            "execute_sql": "INSERT INTO orders (product_id, quantity) VALUES (202, 5)"
        }

        result = convert_named_to_positional_query(sql, params, delimiter)
        self.assertEqual(result, expected)


    def test_no_named_parameters(self):
        sql = "SELECT * FROM users"
        params = {}
        delimiter = "$"

        expected = {
            "positional_sql": "SELECT * FROM users",
            "param_list": [],
            "execute_sql": "SELECT * FROM users"
        }

        result = convert_named_to_positional_query(sql, params, delimiter)
        self.assertEqual(result, expected)

    def test_sql_with_empty_string_parameter(self):
        sql = "SELECT * FROM users WHERE username = :username"
        params = {"username": ""}
        delimiter = ":"

        expected = {
            "positional_sql": "SELECT * FROM users WHERE username = :1",
            "param_list": [""],
            "execute_sql": "SELECT * FROM users WHERE username = "
        }

        result = convert_named_to_positional_query(sql, params, delimiter)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()