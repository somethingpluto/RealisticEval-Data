import pandas as pd

def read_csv_to_dataframe(file_path):
    """
    Reads a CSV file and converts it to a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    try:
        # Read the CSV file
        dataframe = pd.read_csv(file_path)
        return dataframe
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: Could not parse the file.")
    except Exception as e:
        print(f"An error occurred: {e}")