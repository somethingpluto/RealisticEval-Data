def read_tsv_from_stdin():
    reader = csv.reader(sys.stdin, delimiter='\t')
    data = [row for row in reader]
    cols = max(len(row) for row in data)
    # Pad all rows to same length
    data = [row + ([""] * (cols - len(row))) for row in data]
    return data