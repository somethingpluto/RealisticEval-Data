import re
from typing import Dict, Any


def convert_named_to_positional_query(sql: str, params: Dict[str, Any], delimiter: str) -> Dict[str, Any]:
    """
    Convert a SQL query from named parameters to positional parameters,the named parameters flag is the given delimiter.return a dict of positional_sql,param_list,execute_sql

    Args:
        sql (str): The SQL query containing named parameters
        params (Dict[str, Any]): A dictionary mapping named parameters to their values.
        delimiter (str): The delimiter used for the named parameters in the SQL query.such as $,#,:

    Returns:
        Dict[str, Any]: A dictionary containing:
            - 'positional_sql': The SQL query with positional placeholders
            - 'param_list': A list of values corresponding to the positional parameters.
            - 'execute_sql': The SQL query with actual values substituted in.
    """

    result = {}  # Initialize the result dictionary to hold the output.
    param_pattern = rf"\{delimiter}(\w+)"  # Regex pattern to find named parameters.
    positional_sql = sql  # Start with the original SQL string.
    values = []  # List to collect the values for positional parameters.
    index = 1  # Initialize an index for positional parameter numbering.

    # Iterate over all matches of named parameters in the SQL query.
    for match in re.finditer(param_pattern, sql):
        param_name = match.group(1)  # Extract the parameter name from the match.

        # Check if the parameter name exists in the provided params dictionary.
        if param_name in params:
            # Replace the named parameter in the SQL string with its positional counterpart.
            positional_sql = positional_sql.replace(match.group(0), f"{delimiter}{index}")
            # Append the corresponding value to the values list.
            values.append(params[param_name])
            index += 1  # Increment the index for the next positional parameter.
        else:
            # Raise an error if the parameter is not found in the params dictionary.
            raise ValueError(f"Parameter '{param_name}' not found in params dictionary.")

    # Store the modified SQL query with positional parameters in the result.
    result["positional_sql"] = positional_sql
    execute_sql = positional_sql  # Start with the positional SQL for substitution.

    # Replace positional placeholders with their actual values for execution.
    for index, v in enumerate(values):
        execute_sql = execute_sql.replace(f"{delimiter}{index + 1}", str(v))

    # Return the final result containing the positional SQL, parameter list, and executed SQL.
    return {
        "positional_sql": positional_sql,
        "param_list": values,
        "execute_sql": execute_sql
    }
