import os


def delete_non_python_and_ipynb_files(directory):
    """
    删除指定目录下所有非 Python (.py) 和非 Jupyter Notebook (.ipynb) 文件

    :param directory: 需要检查的目录路径
    """
    # 确保目录存在
    if not os.path.isdir(directory):
        print(f"目录 '{directory}' 不存在。")
        return

    # 遍历目录中的所有文件和子目录
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # 如果是文件且扩展名不是.py或.ipynb，则删除该文件
        if os.path.isfile(file_path) and not (filename.endswith('.py') or filename.endswith('.ipynb')):
            try:
                os.remove(file_path)
                print(f"已删除文件: {file_path}")
            except Exception as e:
                print(f"无法删除文件 {file_path}: {e}")