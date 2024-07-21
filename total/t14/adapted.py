import os
import glob
import json

def list_json_reports(directory, keyword="report"):
    """
    在指定目录中列出所有包含特定关键字的 JSON 文件名。
    """
    pattern = os.path.join(directory, f'*{keyword}*.json')
    json_files = glob.glob(pattern)
    return json_files

def select_file(files):
    """
    显示可用文件并提示用户通过索引选择一个文件。
    """
    if not files:
        print("未找到合适的 JSON 文件。")
        return None

    print("请选择一个要加载的 JSON 文件：")
    for idx, file_name in enumerate(files):
        print(f"{idx}: {file_name}")

    try:
        selected_index = int(input("请输入您想读取的 JSON 文件的编号："))
        return files[selected_index]
    except (ValueError, IndexError):
        print("选择无效。请输入一个有效的编号。")
        return None

def read_json_file(file_path):
    """
    读取并返回一个 JSON 文件的内容。
    """
    if file_path is None:
        return None

    with open(file_path, 'r') as file:
        content = json.load(file)
    return content

def pick_json_file(parent_directory):
    json_files = list_json_reports(parent_directory)
    selected_file_path = select_file(json_files)
    return read_json_file(selected_file_path)
