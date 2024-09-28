import re


def prepare_query(sql: str, params: dict) -> tuple:
    """
    This function modifies a SQL query string containing named parameters
    (like $name, $age) into a format compatible with libraries that require
    positional parameters (like $1, $2, etc.), such as asyncpg. It returns
    a tuple containing the modified SQL string and a list of parameter values
    ordered according to their new positions in the query.
    For example:
        input:
            sql: SELECT * FROM users WHERE id = $user_id AND status = $status
            params: {'user_id': 42,'status': 'active'}
        output:
            SELECT * FROM users WHERE id = $1 AND status = $2,[42, 'active']

    Args:
        sql (str): The original SQL query string with named parameters.
        params (dict): A dictionary mapping parameter names to their values.

    Returns:
        tuple: A tuple where the first element is the modified SQL query string with positional parameters, and the second element is a list of parameter values sorted according to the order of the positional parameters.
    """