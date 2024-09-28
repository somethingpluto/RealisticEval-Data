def convert_csv_values(row):
    # Convert all numeric values in the row
    return {key: value.replace(',', '.') if value.replace(',', '', 1).replace('-', '', 1).isdigit() else None for key, value in row.items()}