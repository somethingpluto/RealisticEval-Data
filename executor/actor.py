def get_suffix():
    if language == "python":
        return "py"
    elif language == "javascript":
        return "js"
    elif language == "typescript":
        return "ts"
    elif language == "java":
        return "java"
    elif language == "c&cpp":
        return "c&cpp"


def check_dir(dir_path):
    answer_file_path = f"{dir_path}/answer.{get_suffix()}"
    test_file_path = f"{dir_path}/test.{get_suffix()}"


if __name__ == '__main__':
    task_id = ""
    language = ""
