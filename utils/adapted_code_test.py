import os
import shutil
import subprocess


def getTestCommand(language, file_path):
    command = []
    if language == "python":
        command.extend(['pytest', '-vs', file_path])
    return command


def getCoverageCommand(language):
    command = []
    if language == "python":
        command.extend(['pytest', f'--cov=.', '--cov-branch', '--cov-report=json'])
    return command


def create_test_temp_env():
    # 读取test文件内容
    with open(f"{task_dir_path}/test/test.{TASK_SUFFIX}", "r", encoding="utf8") as test_file:
        test_content = test_file.read()

    # 读取adapted 文件内容
    with open(f"{task_dir_path}/adapted.{TASK_SUFFIX}", "r", encoding="utf8") as adapted_file:
        adapted_file = adapted_file.read()

    # 检测文件是否存在 不存在则创建
    if not os.path.exists(f"{task_dir_path}/temp"):
        try:
            # 如果目录不存在则创建
            os.makedirs(f"{task_dir_path}/temp")
        except OSError as e:
            print(f"Failed to create directory {task_dir_path}/temp: {e}")

    with open(f"{task_dir_path}/temp/test_temp.{TASK_SUFFIX}", "w", encoding="utf8") as temp_file:
        temp_file.write(test_content)
        temp_file.write("\n")
        temp_file.write(adapted_file)
        temp_file.flush()


def execute_pytest():
    # 切换到对应的工作目录
    os.chdir(task_dir_path)
    # 执行pytest命令
    command = getTestCommand(TASK_LANGUAGE, f"./temp/test_temp.{TASK_SUFFIX}")
    result = subprocess.run(command, capture_output=True, text=True)
    # 获取输出
    stdout = result.stdout
    stderr = result.stderr
    print("STDOUT:")
    print(stdout)


def execute_pytest_coverage():
    os.chdir(f"{task_dir_path}/temp")
    command = getCoverageCommand(TASK_LANGUAGE)
    result = subprocess.run(command, capture_output=True, text=True)
    # 获取输出
    stdout = result.stdout
    print("STDOUT:")
    print(stdout)


def execute_clear():
    try:
        # 删除目录及其内容
        shutil.rmtree(f"{task_dir_path}/.pytest_cache")
        shutil.rmtree(f"{task_dir_path}/temp/.pytest_cache")
        os.remove(f"{task_dir_path}/temp/.coverage")
        print("intermediate file success deleted")
    except OSError as e:
        print(f"Error: {task_dir_path} : {e.strerror}")


if __name__ == '__main__':
    TASK_LANGUAGE = "python"
    TASK_ID = "259"
    TASK_SUFFIX = "py"
    task_dir_path = os.path.abspath(f"../total_{TASK_LANGUAGE}/t{TASK_ID}")
    create_test_temp_env()
    execute_pytest()
    execute_pytest_coverage()
    execute_clear()
