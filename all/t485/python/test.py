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
