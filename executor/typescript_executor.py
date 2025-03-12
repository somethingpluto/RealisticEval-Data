import argparse
import json
import os
import re
import subprocess
import time
from pathlib import Path

import pandas as pd
from tqdm import tqdm

TYPESCRIPT_RUN_ENV = "../envs/typescript/test_item/"


class TypeScriptExecutor:
    def __init__(self, model_name, type):
        self._env_path = TYPESCRIPT_RUN_ENV
        self.model_name = model_name
        self.type = type
        self.language = "typescript"
        self.answer_file_path = self._generate_answer_file_path()

    def _generate_answer_file_path(self):
        return rf"E:\code\code_back\python_project\llm\qa\model_answer\{self.model_name}_answer\{self.language}_answer_{self.type}.jsonl"

    def batch_run(self):
        result_list = []
        with open(self.answer_file_path, "r", encoding="utf8") as file:
            json_lines = [line.strip() for line in file.readlines()]
            for item in json_lines:
                result_list.append(json.loads(item))
        for item in tqdm(result_list):
            try:
                task_id = item["task_id"]
                language_item = item['language_version_list']["typescript"]
                answer_list = language_item["answer_list"]
                test_code = language_item["test_code"]
                addition_info = language_item["addition_info"]
                # 生成每个测试问题的测试文件文件
                for index, answer in enumerate(answer_list):
                    code = answer['response_code']
                    if code == None or code == "":
                        continue
                    with open(TYPESCRIPT_RUN_ENV + f"/{task_id}.test.ts", "w", encoding="utf8") as file:
                        file.write(addition_info)
                        file.write(code)
                        file.write("\n")
                        file.write(test_code)
                        file.write("\n")
                        file.flush()
            except Exception as e:
                print(e)
                continue
        # 2.执行命令
        self._execute()
        time.sleep(2)
        # 3.去除颜色
        with open("../envs/typescript/jest-results.json", "r", encoding="utf8") as read_json_file:
            result_content = read_json_file.read()
        with open("../envs/typescript/jest-results.json", "w", encoding="utf8") as write_json_file:
            write_json_file.write(self._remove_color_codes(result_content))
            write_json_file.flush()
        # 4.解析结果文件
        self.parse_result_json_file()

    def _execute(self):
        command = self._generate_command()
        print(command)
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
            stdout, stderr = process.communicate(timeout=60)
            print(stdout)
            print(stderr)
            print("Process completed with return code:", process.returncode)
        except subprocess.TimeoutExpired:
            print("Process is being killed after timeout")
            process.kill()

    def _get_file_disk_flag(self):
        # 获取当前文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 分离盘符和路径
        drive_letter = os.path.splitdrive(current_file_path)[0]
        return drive_letter

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

    def _generate_command(self):
        driver_flag = self._get_file_disk_flag()
        command = f"{driver_flag} && cd {driver_flag}/code/code_back/python_project/RealisticEval-Data/envs/typescript/test_item && npm run test-silent"
        return command

    def parse_result_json_file(self):
        file_data = []
        result_file_path = "../envs/typescript/jest-results.json"
        with open(result_file_path, "r", encoding="utf8") as json_file:
            test_data = json.load(json_file)
        result_list = test_data["testResults"]
        for result in result_list:
            temp_data = {}
            task_id = result["name"].split("\\")[-1].split(".")[0]
            temp_data["task_id"] = task_id
            if result["status"] == "passed":
                temp_data["result_return_code"] = 0
            else:
                temp_data["result_return_code"] = 1
            temp_data["model"] = args.model_name
            file_data.append(temp_data)
        pd.DataFrame(file_data).to_csv(
            f"../model_answer/{self.model_name}/{self.type}/{self.model_name}_typescript_{self.type}.csv", index=False)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, help="model_answer_file_path", required=True)
    parser.add_argument("--type", type=str, help="type pass1 or pass10", required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    executor = TypeScriptExecutor(args.type, args.model_name)
    executor.batch_run()
