import csv
import os


def csv_to_sql_insert(csv_file_path):
    # Extract the table name from the CSV file name, removing the suffix
    table_name = os.path.splitext(os.path.basename(csv_file_path))[0]

    # Open the CSV file and read its contents
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)

        # Get the header (first row) for column names
        headers = next(reader)

        # Prepare the SQL insert statement
        insert_statements = []

        for row in reader:
            values = []
            for value in row:
                # Handle different types of values (e.g., strings, numbers)
                if value.isdigit():  # If value is a digit, no quotes needed
                    values.append(value)
                else:  # Assume it's a string otherwise
                    escaped_value = value.replace("'", "''")  # Escape single quotes
                    values.append(f"'{escaped_value}'")  # Use double quotes outside

            # Join column names and values to form an INSERT statement
            insert_statement = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(values)});"
            insert_statements.append(insert_statement)

    # Combine all insert statements into a single output
    return '\n'.join(insert_statements)
