import argparse
import json
import os
import re
import subprocess

import pandas as pd
from tqdm import tqdm

from executor.utils import append_row_to_xlsx

TYPESCRIPT_RUN_ENV = "../envs/typescript"


class TypeScriptExecutor:
    def __init__(self, type, model_name=""):
        self._env_path = TYPESCRIPT_RUN_ENV
        self.model_name = model_name
        self.type = type
        self.file_path = f"{self._env_path}/test.test.ts"
        self.language = "typescript"

    def single_run(self, code, test_code):
        with open(self.file_path, "w", encoding="utf8") as file:
            file.write(code)
            file.write("\n")
            file.write(test_code)
            file.write("\n")
            file.flush()
            self._execute()

    def batch_run(self, file_path):
        result_list = []
        data_list = []
        with open(file_path, "r", encoding="utf8") as file:
            json_lines = [line.strip() for line in file.readlines()]
            for item in json_lines:
                result_list.append(json.loads(item))

        for item in tqdm(result_list[180:]):
            try:
                print(item["task_id"])
                language_item = item['language_version_list']["typescript"]
                answer_list = language_item["answer_list"]
                test_code = language_item["test_code"]
                addition_info = language_item["addition_info"]
                for index, answer in enumerate(answer_list):
                    code = answer['response_code']
                    if code == None or code == "":
                        continue
                    with open(self.file_path, "w", encoding="utf8") as file:
                        file.write(code)
                        file.write("\n")
                        file.write(test_code)
                        file.write("\n")
                        file.flush()
                    process, stdout, stderr, returncode = self._execute()
                    process.kill()
                    item["result_return_code"] = returncode
                    item["stderr"] = self._remove_color_codes(stderr)
                    item["stdout"] = self._remove_color_codes(stdout)
                    item["answer_index"] = index
                    item["model"] = answer["model_name"]
                    with open(f"{self._env_path}/test.test.ts", "r", encoding="utf8") as f:
                        item["full_content"] = f.read()
                    data_list.append(item)
                    with open(
                            f"../analysis/model_answer_result/{self.model_name}/{self.type}/{self.model_name}_{self.language}_{self.type}.csv",
                            "a+", encoding="utf8") as file:
                        file.write(f"{item['task_id']},{returncode},{answer['model_name']}\n")
            except Exception as e:
                print(e)
                continue
        result_data = pd.DataFrame(data_list)
        result_data.to_excel(
            f"../analysis/model_answer_result/{self.model_name}/{self.type}/{self.model_name}_{self.language}_{self.type}.xlsx",
            engine="xlsxwriter")
        result_data.to_excel(
            rf"C:\Users\pluto\Desktop\temp\{self.model_name}\{self.model_name}_{self.language}_{self.type}.xlsx",
            engine="xlsxwriter")

    def _execute(self):
        command = self._generate_command()
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            encoding='utf-8',
            errors='ignore'  # 忽略编码错误
        )
        try:
            # 等待进程结束或超时
            stdout, stderr = process.communicate(timeout=20)
            print(stdout)
            print(stderr)
            print("Process completed with return code:", process.returncode)
            return process, stdout, stderr, process.returncode
        except subprocess.TimeoutExpired:
            print("Process is being killed after timeout")
            process.kill()

    def _remove_color_codes(self, text):
        """
        Removes ANSI color codes from the given text.

        Args:
        text (str): The text containing ANSI color codes.

        Returns:
        str: The cleaned text without color codes.
        """
        # ANSI color code regex pattern
        ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', text)

    def _get_file_disk_flag(self):
        # 获取当前文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 分离盘符和路径
        drive_letter = os.path.splitdrive(current_file_path)[0]
        return drive_letter

    def _generate_command(self):
        driver_flag = self._get_file_disk_flag()
        # TODO: 替换为 本机中 RealisticEval-Data\envs\typescript 文件中的路径 不必填写盘符
        command = rf"{driver_flag} && cd {driver_flag}/code/code_back/python_project/RealisticEval-Data/envs/typescript && npm run test-silent"
        return command


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, help="model_answer_file_path", required=True)
    parser.add_argument("--type", type=str, help="type pass1 or pass10", required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    executor = TypeScriptExecutor(args.type, args.model_name)
    file_path = rf"E:\code\code_back\python_project\llm\qa\{args.model_name}_answer\typescript_answer_{args.type}.jsonl"
    executor.batch_run(file_path)
