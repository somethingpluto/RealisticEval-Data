import argparse
import json
import os
import re
import subprocess

import pandas as pd
from tqdm import tqdm

from executor.utils import append_row_to_xlsx

JAVA_RUN_ENV = "../envs/java/src"


class JavaExecutor:
    def __init__(self, type, model_name=""):
        self._env_path = JAVA_RUN_ENV
        self.model_name = model_name
        self.type = type
        self.language = "java"

    def single_run(self, code: str, test_code: str):
        # 向Answer.java文件写入
        with open(f"{JAVA_RUN_ENV}/main/java/org/real/temp/Answer.java", "w", encoding="utf8") as code_file:
            code_file.write(code)
            code_file.flush()
        # 向Test.java文件写入写入
        with open(f"{JAVA_RUN_ENV}/test/java/org/real/temp/Tester.java", "w", encoding="utf8") as test_file:
            test_file.write(test_code)
            test_file.flush()
        self._execute()

    def batch_run(self, file_path):
        result_list = []
        data_list = []
        with open(file_path, "r", encoding="utf8") as file:
            json_lines = [line.strip() for line in file.readlines()]
            for item in json_lines:
                result_list.append(json.loads(item))

        for item in tqdm(result_list):
            try:
                print(item["task_id"])
                language_item = item['language_version_list']["java"]
                answer_list = language_item["answer_list"]
                test_code = language_item["test_code"]
                addition_info = language_item["addition_info"]
                for index, answer in enumerate(answer_list):
                    code = answer['response_code']
                    if code == None or code == "":
                        continue
                    with open(f"{JAVA_RUN_ENV}/main/java/org/real/temp/Answer.java", "w", encoding="utf8") as code_file:
                        code_file.write(code)
                        code_file.flush()
                    # 向Test.java文件写入写入
                    with open(f"{JAVA_RUN_ENV}/test/java/org/real/temp/Tester.java", "w", encoding="utf8") as test_file:
                        test_file.write(test_code)
                        test_file.flush()
                    stdout, stderr, returncode = self._execute()
                    item["result_return_code"] = returncode
                    item["stderr"] = stderr
                    item["stdout"] = stdout
                    with open(f"{JAVA_RUN_ENV}/main/java/org/real/temp/Answer.java", "r", encoding="utf8") as code_file:
                        item["Answer"] = code_file.read()
                    with open(f"{JAVA_RUN_ENV}/test/java/org/real/temp/Tester.java", "r", encoding="utf8") as test_file:
                        item["Tester"] = test_file.read()
                    xlsx_data_list = item.values()
                    print(xlsx_data_list)
                    append_row_to_xlsx(
                        f"../analysis/model_answer_result/{self.model_name}/{self.type}/{self.model_name}_{self.language}_{self.type}.xlsx",
                        xlsx_data_list)
                    append_row_to_xlsx(
                        rf"C:\Users\pluto\Desktop\temp\{self.model_name}\{self.model_name}_{self.language}_{self.type}.xlsx",
                        xlsx_data_list)
            except Exception as e:
                print(e)
                continue
        data = pd.DataFrame(data_list)
        data.to_excel(f"../analysis/model_answer_result/{self.model_name}/{self.model_name}_java.xlsx",
                      engine='xlsxwriter')

    def _execute(self):
        command = self._generate_command()
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            encoding='utf-8',
            errors='ignore'  # 忽略编码错误
        )
        try:
            # 等待进程结束或超时
            stdout, stderr = process.communicate(timeout=10)
            print(stdout)
            print(stderr)
            print("Process completed with return code:", process.returncode)
            return stdout, stderr, process.returncode
        except subprocess.TimeoutExpired:
            print("Process is being killed after timeout")
            process.kill()

    def _generate_command(self):
        driver_flag = self._get_file_disk_flag()
        # TODO: 替换为 本机中 RealisticEval-Data\envs\javascript 文件中的路径 不必填写盘符
        command = f"{driver_flag} && cd {driver_flag}/code/code_back/python_project/RealisticEval-Data/envs/java && mvn -Dstyle.color=never test"
        return command

    def _get_file_disk_flag(self):
        # 获取当前文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 分离盘符和路径
        drive_letter = os.path.splitdrive(current_file_path)[0]
        return drive_letter


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, help="model_answer_file_path", required=True)
    parser.add_argument("--type", type=str, help="type pass1 or pass10", required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    executor = JavaExecutor(args.type, args.model_name)
    file_path = rf"E:\code\code_back\python_project\llm\qa\{args.model_name}_answer\java_answer_{args.type}.jsonl"
    executor.batch_run(file_path)
