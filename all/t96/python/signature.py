def changed_clef(abc: str, clef: str = "bass") -> str:
    """
    Modify the ABC string by inserting the specified clef (e.g., "clef=bass")
    after the tone line (K:), or "bass" if no clef is specified.

    Args:
        abc (str): The ABC notation string.
        clef (str): The clef to set (default is "bass").

    Returns:
        str: The updated ABC notation string with the new clef.
    """