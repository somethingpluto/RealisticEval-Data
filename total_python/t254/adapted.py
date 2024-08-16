import pandas as pd


def transpose_and_merge_rows(df, row_indices, column_labels=None):
    """
    Selects specific rows from a DataFrame, transposes them, and merges them into a new DataFrame.

    Args:
    df (pd.DataFrame): The original DataFrame.
    row_indices (list of int): Indices of the rows to select and transpose.
    column_labels (list of str, optional): Column labels for the new DataFrame after transposition.
        If None, the original row indices will be used as column labels.

    Returns:
    pd.DataFrame: A new DataFrame where each selected row from the original DataFrame
        becomes a column in the new DataFrame.
    """
    # Select and transpose the specific rows
    transposed_data = df.iloc[row_indices].transpose()

    # If column_labels are provided, rename the columns
    if column_labels:
        transposed_data.columns = column_labels
    else:
        # Otherwise, use the original indices as column names
        transposed_data.columns = [f'Row_{idx}' for idx in row_indices]

    return transposed_data
