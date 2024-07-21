import re

def get_name(path):
    # Replace all forward slashes with underscores and strip leading underscores
    new_path = path.replace("/", "_").lstrip("_")

    # Use regular expression to remove specified directory names followed by an underscore
    remove_items = ["artifacts", "bundle", "environments", "include", "resources", "workspace", "items", "properties"]
    pattern = f"({'|'.join(remove_items)})_"
    new_path = re.sub(pattern, "", new_path)

    # Remove trailing '_items' if present
    new_path = re.sub(r"_items$", "", new_path)

    return new_path
