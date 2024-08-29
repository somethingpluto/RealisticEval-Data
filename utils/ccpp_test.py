import os
import subprocess


def create_test_temp_env():
    # 读取test文件夹下的内容
    with open(f"{task_dir_path}/test/test.{TASK_SUFFIX}", "r", encoding="utf8") as test_file:
        test_content = test_file.read()

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
        temp_file.write("#define CATCH_CONFIG_MAIN\n")
        temp_file.write("#include \"../../lib/catch.hpp\"\n")
        temp_file.write(f"#include \"../{TASK_SCOPE}.cpp\"")
        temp_file.write("\n")
        temp_file.write(test_content)
        temp_file.flush()


def execute_command():
    work_path = f"{task_dir_path}/{TASK_SCOPE}_temp"
    os.chdir(work_path)
    # 构建完整命令
    args = ["g++", "adapted.test.cpp", "-o", "adapted.test"]
    # 执行命令
    result = subprocess.run(args, capture_output=True, text=True)

    # 检查是否成功
    if result.stdout:  # 如果有标准输出，打印它
        print("Standard Output:\n", result.stdout)
    if result.stderr:  # 如果有错误输出，打印它
        print("Standard Error:\n", result.stderr)

    result = subprocess.run(["adapted.test"], capture_output=True, text=True)
    # 检查是否成功
    # 打印标准输出和标准错误
    if result.stdout:  # 如果有标准输出，打印它
        print("Standard Output:\n", result.stdout)
    if result.stderr:  # 如果有错误输出，打印它
        print("Standard Error:\n", result.stderr)


if __name__ == '__main__':
    TASK_LANGUAGE = "c&cpp"
    TASK_ID = "202"
    TASK_SUFFIX = "cpp"
    TASK_SCOPE = "adapted"
    task_dir_path = os.path.abspath(f"E:/Desktop/Github desktop backup/RealisticEval-Data/total_{TASK_LANGUAGE}/t{TASK_ID}")
    create_test_temp_env()
    execute_command()
