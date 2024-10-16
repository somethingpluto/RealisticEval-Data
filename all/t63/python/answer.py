def convert_dataframe_to_markdown(df, md_path):
    # Construct the header row
    headers = "| " + " | ".join(df.columns) + " |\n"
    # Construct the separator row
    separators = "| " + " | ".join(["---"] * len(df.columns)) + " |\n"
    # Combine headers and separators
    markdown = headers + separators

    # Build markdown table body
    for _, row in df.iterrows():
        markdown += "| " + " | ".join(str(value) for value in row) + " |\n"

    # Write markdown to file
    with open(md_path, "w") as handle:
        handle.write(markdown)

    return markdown
