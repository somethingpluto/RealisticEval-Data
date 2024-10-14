def get_css_from_sheet(sheet: str) -> str:
    """
    Extract all the CSS rules from a given CSSStyleSheet and concatenate them into a string.

    Args:
        sheet (CSSStyleSheet): The stylesheet object from which to extract CSS rules.

    Returns:
        str: A single string containing all CSS rules, or an empty string if the sheet is invalid or inaccessible.
    """