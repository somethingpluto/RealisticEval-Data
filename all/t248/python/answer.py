import json


def sanitize_data(data, key_to_remove=None
                  ):
    """Recursively sanitize a dictionary by removing specific keys."""
    if key_to_remove is None:
        key_to_remove = {"email", "pc_conflicts", "metadata", "eligible_student_paper_prize", "talk_poster",
                         "submitted_at",
                         "decision", "status", "submitted", "submission"}
    if isinstance(data, dict):
        return {key: sanitize_data(value) for key, value in data.items() if key not in key_to_remove}
    elif isinstance(data, list):
        return [sanitize_data(value) for value in data]
    else:
        return data
