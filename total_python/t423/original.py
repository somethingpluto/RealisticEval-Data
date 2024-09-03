def writeFile(lines, filename, helper: bool = False):
    lines = [line + '\n' for line in lines]
    if helper:
        filename = f"build/{filename}.tex"
    else:
        filename = f"assets/graphs/{filename}.tex"

    try:
        with open(filename, "r", encoding="utf-8") as readFile:
            existingLines = readFile.readlines()
    except FileNotFoundError:
        existingLines = []

    if existingLines != lines:
        with open(filename, "w+", encoding="utf-8") as outFile:
            outFile.writelines(lines)
    else:
        print(f"No changes to {filename}")