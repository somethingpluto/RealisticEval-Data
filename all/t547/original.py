def calculate_column_widths(data):
    widths = [0] * len(data[0])
    for row in data:
        for idx, col in enumerate(row):
            widths[idx] = max(widths[idx], len(col))
    return widths