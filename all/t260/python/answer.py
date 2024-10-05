import pandas as pd


def process_csv(file_path, output_path):
    """
    Processes a CSV file and removes rows with two or more empty columns.

    Parameters:
    file_path (str): The path to the input CSV file.
    output_path (str): The path where the processed CSV file will be saved.

    Returns:
    None
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Count the number of empty columns in each row
        empty_count = df.isnull().sum(axis=1)

        # Filter the DataFrame to keep only rows with less than 2 empty columns
        filtered_df = df[empty_count < 2]

        # Save the processed DataFrame to a new CSV file
        filtered_df.to_csv(output_path, index=False)

    except pd.errors.EmptyDataError:
        # Handle the case of an empty CSV
        with open(output_path, 'w') as f:
            f.write("")  # Write an empty file

    except pd.errors.ParserError:
        # Handle parsing errors (e.g., inconsistent columns in rows)
        print("Error: The input CSV has inconsistent row lengths. Please check the input data.")