import csv
import os

def csv_to_sql_insert(csv_file_path: str) -> str:
    # Get the table name from the CSV file name
    table_name = os.path.splitext(os.path.basename(csv_file_path))[0]

    # Open the CSV file and read the header row
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

    # Initialize the SQL INSERT statement
    sql = f"INSERT INTO {table_name} ("
    values_clause = "VALUES ("

    # Read the rest of the rows and generate the SQL INSERT statement
    for index, row in enumerate(reader):
        if index > 0:
            sql += ", " + table_name + "." + ",".join(row)
            values_clause += ", " + ",".join(map(str, row))
        else:
            sql += ", ".join(table_name + "." + col for col in row)

    # Close the SQL INSERT statement
    sql += ")"
    values_clause += ")"

    # Combine the SQL INSERT statement and the values clause
    sql += "\n" + values_clause

    return sql
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