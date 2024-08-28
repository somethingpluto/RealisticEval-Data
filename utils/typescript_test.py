import os
import subprocess


def create_test_temp_env():
    # 读取test文件夹下的内容
    with open(f"{task_dir_path}/test/test.{TASK_SUFFIX}", "r", encoding="utf8") as test_file:
        test_content = test_file.read()

    # 读取指定task scope的文件内容
    with open(f"{task_dir_path}/{TASK_SCOPE}.{TASK_SUFFIX}", "r", encoding="utf8") as scope_file:
        scope_content = scope_file.read()

    temp_dir_path = ""
    # 检测文件是否存在 不存在则创建
    if TASK_SCOPE == "original":
        temp_dir_path = f"{task_dir_path}/original_temp"
    elif TASK_SCOPE == "adapted":
        temp_dir_path = f"{task_dir_path}/adapted_temp"
    if not os.path.exists(temp_dir_path):
        try:
            # 如果目录不存在则创建
            os.makedirs(temp_dir_path)
        except OSError as e:
            print(f"Failed to create directory {temp_dir_path}: {e}")

    with open(f"{temp_dir_path}/{TASK_SCOPE}.test.{TASK_SUFFIX}", "w", encoding="utf8") as temp_file:
        temp_file.write(test_content)
        temp_file.write("\n")
        temp_file.write(scope_content)
        temp_file.flush()


if __name__ == '__main__':
    TASK_LANGUAGE = "typescript"
<<<<<<< HEAD
    TASK_ID = "150"
=======
    TASK_ID = "341"
>>>>>>> main
    TASK_SUFFIX = "ts"
    TASK_SCOPE = "adapted"
    task_dir_path = os.path.abspath(f"../total_{TASK_LANGUAGE}/t{TASK_ID}")
    create_test_temp_env()
