def list_of_dict_to_markdown(builder: io.IOBase, data: list[dict[str, ScalarTypes]], indent: int = 0):
    """
    Create a markdown table. Assumes dict are compatible (have similar keys) and shallow (no dicts of dict values)
    """
    row_id = 0

    column_widths: dict[str, int] = {}
    for schema in data:
        column_widths = column_widths | {key: 0 for key in schema.keys()}

    for datum in data:
        for key, value in datum.items():
            # TODO: doesn't handle complex types (and maybe can't? markdown doesn't support nested tables, AFAIK)
            max_width = max(len(str(key)), len(str(value)))
            if max_width > column_widths[key]:
                column_widths[key] = max_width

    for datum in data:
        include_header = row_id == 0
        builder.write(dict_to_markdown(datum, include_header, column_widths, indent))
        row_id += 1
