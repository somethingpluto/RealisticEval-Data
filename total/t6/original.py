# Generated using ChatGPT 3.5


def get_name(path):
    new_path = path.replace("/", "_").lstrip("_")
    for remove_item in [
        "artifacts",
        "bundle",
        "environments",
        "include",
        "resources",
        "workspace",
        "items",
        "properties",
    ]:
        new_path = new_path.replace(f"{remove_item}_", "")

    new_path = new_path.replace("_items", "")

    return new_path