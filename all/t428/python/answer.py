import ast

def parse_type_hint(type_hint_string):
    """
    Parses a Python type hint string and returns the individual types as a list of strings.

    Args:
        type_hint_string (str): The type hint string to parse.

    Returns:
        list: The individual types parsed from the type hint string.

    Example:
        type_hint = "Union[typing.List[str], typing.Dict[str, int], Tuple[int, str], Optional[int]]"
        parsed_types = parse_type_hint(type_hint)
        print(parsed_types)
        # Output: ['Union', 'typing.List', 'str', 'typing.Dict', 'str', 'int', 'Tuple', 'int',
                   'str', 'Optional', 'int']
    """
    # Create a source function definition with the type hint string
    source = f'def f() -> {type_hint_string}: pass'
    # Parse the source code into an Abstract Syntax Tree (AST)
    tree = ast.parse(source)

    # List to store the parsed type strings
    type_strings = []

    def process_node(node, qual_names=None):
        """
        Recursively processes the AST nodes and extracts the type names.

        Args:
            node (ast.AST): The AST node to process.
            qual_names (list): A list of qualified names encountered during processing.

        Returns:
            None
        """
        # Initialize qualified names if not provided
        qual_names = qual_names or []

        if isinstance(node, ast.Name):
            # Add simple type names (e.g., str, int)
            type_strings.append('.'.join(reversed(qual_names + [node.id])))

        elif isinstance(node, ast.Subscript):
            # Process the value and slice of a subscript (e.g., List[str])
            process_node(node.value, qual_names)
            process_node(node.slice, qual_names)

        elif isinstance(node, ast.Attribute):
            # Process attributes (e.g., typing.List)
            process_node(node.value, qual_names + [node.attr])

        elif isinstance(node, ast.Tuple):
            # Process each element in a tuple type hint
            for elt in node.elts:
                process_node(elt, qual_names)

    # Extract the return annotation from the parsed tree
    returns_annotation = tree.body[0].returns
    # Process the return annotation to fill type_strings
    process_node(returns_annotation)

    return type_strings