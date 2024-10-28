import argparse
import json
import os
import subprocess
import time

import pandas as pd
from tqdm import tqdm

from executor.utils import append_row_to_xlsx

CCPP_RUN_ENV = "../envs/c&cpp"
import subprocess


def kill_process_by_name(process_name):
    # 查找进程
    try:
        # 使用 tasklist 命令获取当前运行的进程列表
        tasklist_output = subprocess.check_output("tasklist", text=True)

        # 检查进程是否在任务列表中
        if process_name in tasklist_output:
            print(f"Process '{process_name}' found. Attempting to terminate...")
            # 使用 taskkill 命令杀死进程
            subprocess.run(["taskkill", "/F", "/IM", process_name])
            print(f"Process '{process_name}' has been terminated.")
        else:
            print(f"Process '{process_name}' not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

class CCPPExecutor:
    def __init__(self, type, model_name=""):
        self._env_path = CCPP_RUN_ENV
        self.model_name = model_name
        self.type = type
        self.language = "c&cpp"

    def single_run(self, code, test_code):
        with open(f"{self._env_path}/solution.cpp", "w", encoding="utf8") as temp_file:
            temp_file.write(code)
            temp_file.flush()

        with open(f"{self._env_path}/answer_check.cpp", "w", encoding="utf8") as file:
            file.write("#define CATCH_CONFIG_MAIN\n")
            file.write("#include \"./lib/catch.hpp\"\n")
            file.write("#include \"./solution.cpp\"\n")
            file.write(test_code)
            file.flush()
            self._execute()

    def batch_run(self, file_path):
        result_list = []
        data_list = []
        with open(file_path, "r", encoding="utf8") as file:
            json_lines = [line.strip() for line in file.readlines()]
            for item in json_lines:
                result_list.append(json.loads(item))

        for item in tqdm(result_list[150:]):
            try:
                print(item["task_id"])
                language_item = item['language_version_list']["c&cpp"]
                answer_list = language_item["answer_list"]
                test_code = language_item["test_code"]
                addition_info = language_item["addition_info"]
                for index, answer in enumerate(answer_list):
                    code = answer['response_code']
                    if code is None or code == "":
                        continue
                    with open(f"{self._env_path}/answer_check.cpp", "w", encoding="utf8") as file:
                        file.write("#define CATCH_CONFIG_MAIN\n")
                        file.write("#include \"./lib/catch.hpp\"\n")
                        file.write(addition_info)
                        file.write(code)
                        file.write(test_code)
                        file.flush()
                    process, stdout, stderr, returncode = self._execute()
                    process.kill()
                    kill_process_by_name("answer_check.exe")
                    item["result_return_code"] = returncode
                    item["stderr"] = stderr
                    item["stdout"] = stdout
                    item["answer_index"] = index
                    item["model"] = answer["model_name"]
                    with open(f"{self._env_path}/answer_check.cpp", "r", encoding="utf8") as f:
                        item["full_content"] = f.read()
                    with open(
                            f"../analysis/model_answer_result/{self.model_name}/{self.type}/{self.model_name}_{self.language}_{self.type}.csv",
                            "a+", encoding="utf8") as file:
                        file.write(f"{item['task_id']},{returncode},{answer['model_name']}\n")
                    time.sleep(0.5)
                    os.remove(r"E:\code\code_back\python_project\RealisticEval-Data\envs\c&cpp\answer_check.exe")
            except Exception as e:
                print(e)
                continue

    def _execute(self):
        command = self._generate_command()
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            encoding='utf-8',
            errors='ignore',  # 忽略编码错误
            text=True
        )
        try:
            # 等待进程结束或超时
            stdout, stderr = process.communicate(timeout=25)
            print(stdout)
            print(stderr)
            print("Process completed with return code:", process.returncode)
            return process, stdout, stderr, process.returncode
        except subprocess.TimeoutExpired:
            print("Process is being killed after timeout")
            process.kill()

    def _get_file_disk_flag(self):
        # 获取当前文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 分离盘符和路径
        drive_letter = os.path.splitdrive(current_file_path)[0]
        return drive_letter

    def _generate_command(self):
        driver_flag = self._get_file_disk_flag()
        # TODO：替换为 本机中 /code/python_project/RealisticEval-Data/envs 文件中的路径 不必填写盘符
        command = rf'{driver_flag} && cd /code/code_back/python_project/RealisticEval-Data/envs && cd "c&cpp" && g++ answer_check.cpp -o answer_check && answer_check.exe'
        return command


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, help="model_answer_file_path", required=True)
    parser.add_argument("--type", type=str, help="type pass1 or pass10", required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    executor = CCPPExecutor(args.type, args.model_name)
    file_path = rf"E:\code\code_back\python_project\llm\qa\{args.model_name}_answer\c&cpp_answer_{args.type}.jsonl"
    executor.batch_run(file_path)
