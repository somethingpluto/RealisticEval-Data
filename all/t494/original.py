def clean_values(row):
    """Return a new dictionary with no NaN, None, or empty/whitespace-only values."""
    return {k: v for k, v in row.items() if pd.notna(v) and v is not None and v.strip()}