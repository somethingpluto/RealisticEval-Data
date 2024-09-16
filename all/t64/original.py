import csv


def csv_to_line_protocol(csv_file_path, measurement):
    lines = []

    # Prepend DDL statements
    lines.append("# DDL")
    lines.append(f"CREATE DATABASE BikeComputer\n")

    # Prepend DML statements
    lines.append("# DML")
    lines.append(f"# CONTEXT-DATABASE: BikeComputer")
    lines.append(f"# CONTEXT-RETENTION-POLICY: autogen\n")

    start_distance = 0.0

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            converted_row = convert_csv_values(row)

            # Set start distance to zero
            if start_distance == 0: start_distance = float(converted_row['distance'])
            converted_row['distance'] = float(converted_row['distance']) - start_distance

            timestamp = excel_timestamp_to_datetime(converted_row['Timestamp'])
            print(timestamp)
            tags = ''  # Add tags if needed, e.g., 'tag1=value1,tag2=value2'
            fields = ','.join(
                [f'{key}={value}' for key, value in converted_row.items() if key != 'Timestamp' and value is not None])

            line = f'{measurement}{tags} {fields} {timestamp.strftime("%s")}'
            lines.append(line)

    return lines