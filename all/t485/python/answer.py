import re


def prepare_query(sql: str, params: dict) -> tuple:
    """
    This function modifies a SQL query string containing named parameters
    (like $name, $age) into a format compatible with libraries that require
    positional parameters (like $1, $2, etc.), such as asyncpg. It returns
    a tuple containing the modified SQL string and a list of parameter values
    ordered according to their new positions in the query.

    Args:
        sql (str): The original SQL query string with named parameters.
        params (dict[str, T.Any]): A dictionary mapping parameter names to their values.

    Returns:
        tuple[str, list[T.Any]]: A tuple where the first element is the modified SQL query string
                                  with positional parameters, and the second element is a list of
                                  parameter values sorted according to the order of the positional parameters.
    """

    # Find all occurrences of named parameters in the SQL string
    named_params = re.findall(r"\$(\w+)", sql)

    # Remove duplicates while preserving order
    unique_params = list(dict.fromkeys(named_params))

    # Substitute each named parameter with its corresponding positional parameter
    for index, param in enumerate(unique_params, start=1):
        sql = sql.replace(f"${param}", f"${index}")

    # Prepare the list of values corresponding to the order of the positional parameters
    values = [params[param] for param in unique_params if param in params]

    return sql, values
