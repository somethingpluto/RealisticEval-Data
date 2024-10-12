from cssutils import parseString


def get_css_from_sheet(sheet):
    """
    Extracts CSS rules from a given CSS stylesheet.

    Args:
        sheet (str): A string representation of the CSS stylesheet.

    Returns:
        str: A concatenated string of CSS rules.
    """
    # Check if the sheet is a valid CSS string
    if not isinstance(sheet, str):
        return ''

    # Parse the CSS string to get the stylesheet object
    stylesheet = parseString(sheet)

    # Extract the CSS rules and concatenate them
    css_rules = []
    for rule in stylesheet.cssRules:
        css_rules.append(rule.cssText)

    return ''.join(css_rules)
