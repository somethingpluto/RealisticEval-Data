import csv
import os

def csv_to_sql_insert(csv_file_path: str) -> str:
    """
    Converts the contents of a csv file into an SQL insert statement with a table name with the suffix removed.

    Args:
        csv_file_path (str): csv file path

    Returns:
        str: parsed sql str
    """
    table_name = os.path.basename(csv_file_path).split('.')[0]
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        sql_insert = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES "
        for row in csv_reader:
            values = ', '.join([f"'{value}'" for value in row])
            sql_insert += f"({values}), "
        sql_insert = sql_insert.rstrip(', ') + ';'
        return sql_insert
import unittest
import os


class TestCsvToSqlInsert(unittest.TestCase):

    def setUp(self):
        # Create sample CSV files for testing
        self.test_files = {
            'test1.csv': 'id,name,age\n1,Alice,30\n2,Bob,25',
            'test2.csv': 'product_id,product_name,price\n101,Widget,9.99\n102,Gadget,12.49',
            'test3.csv': 'user_id,email\n3,test@example.com\n4,user@domain.com',
            'test4.csv': 'order_id,order_date,total\n1001,2024-09-01,59.99',
            'test5.csv': 'quote_id,quote\n1,"It\'s a beautiful day."\n2,"She said, ""Hello!"""'
        }
        # Create the files on disk
        for filename, content in self.test_files.items():
            with open(filename, 'w') as f:
                f.write(content)

    def tearDown(self):
        # Remove the test files after tests
        for filename in self.test_files:
            os.remove(filename)

    def test_simple_csv(self):
        expected_sql = (
            "INSERT INTO test1 (id, name, age) VALUES ('1', 'Alice', '30');\n"
            "INSERT INTO test1 (id, name, age) VALUES ('2', 'Bob', '25');"
        )
        result = csv_to_sql_insert('test1.csv')
        self.assertEqual(result, expected_sql)

    def test_product_csv(self):
        expected_sql = (
            "INSERT INTO test2 (product_id, product_name, price) VALUES ('101', 'Widget', '9.99');\n"
            "INSERT INTO test2 (product_id, product_name, price) VALUES ('102', 'Gadget', '12.49');"
        )
        result = csv_to_sql_insert('test2.csv')
        self.assertEqual(result, expected_sql)

    def test_email_csv(self):
        expected_sql = (
            "INSERT INTO test3 (user_id, email) VALUES ('3', 'test@example.com');\n"
            "INSERT INTO test3 (user_id, email) VALUES ('4', 'user@domain.com');"
        )
        result = csv_to_sql_insert('test3.csv')
        self.assertEqual(result, expected_sql)

    def test_date_and_decimal_csv(self):
        expected_sql = (
            "INSERT INTO test4 (order_id, order_date, total) VALUES ('1001', '2024-09-01', '59.99');"
        )
        result = csv_to_sql_insert('test4.csv')
        self.assertEqual(result, expected_sql)
if __name__ == '__main__':
    unittest.main()