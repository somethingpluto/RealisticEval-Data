def dataframe_to_markdown(df, md_path):
    markdown = "| " + " | ".join(df.columns) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(df.columns)) + " |\n"

    for _, row in df.iterrows():
        markdown += "| " + " | ".join(str(value) for value in row) + " |\n"

    with open(md_path, "w") as handle:
        handle.write(markdown)

    return markdown