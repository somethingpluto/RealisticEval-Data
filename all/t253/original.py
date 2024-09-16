# generated via ChatGPT: https://chat.openai.com/share/e15a442f-1524-4915-a3d4-5a84e2bb16f3
def log(item):
    # Check if the item is a string or a number (int or float)
    if isinstance(item, (str, int, float)):
        print(item)
    # Check if the item is an object that can be serialized to JSON
    elif isinstance(item, (dict, list)):
        print(json.dumps(item))
    else:
        # If the item is neither, print an error message
        print("Error: Unsupported type for logging.")