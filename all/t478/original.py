def class_to_dict(obj) -> dict[str, Any]:
    """
    Converts classes to dict

    Function written with ChatGPT 3.5 Turbo
    """
    if is_dataclass(obj):
        return obj.__dict__
    if isinstance(obj, type):
        return {k: v for k, v in obj.__dict__.items() if not k.startswith("__")}
    return obj.__dict__