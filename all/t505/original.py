def to_snake_case(input_string: str) -> str:
    """
    Converts CamelCase strings into snake_case (created by ChatGPT)
    :param input_string: String to convert
    :return: String converted to snake case
    """
    return "".join(["_" + c.lower() if c.isupper() else c for c in input_string]).lstrip("_")