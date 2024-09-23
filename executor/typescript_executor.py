import json
import os
import re
import subprocess

import pandas as pd
from tqdm import tqdm

import executor.executor_config as config


class TypeScriptExecutor:
    def __init__(self, model_name=""):
        self._env_path = config.TYPESCRIPT_RUN_ENV
        self.model_name = model_name
        self.file_path = f"{self._env_path}/test.test.ts"

    def single_run(self, code, test_code):
        with open(self.file_path, "w", encoding="utf8") as file:
            file.write(code)
            file.write("\n")
            file.write(test_code)
            file.write("\n")
            file.flush()
            self._execute()

    def batch_run(self, file_path):
        data_list = []
        with open(file_path, "r", encoding="utf8") as file:
            result_list = json.load(file)

        for item in tqdm(result_list):
            try:
                print(item["task_id"])
                test_code = item['test_code']
                answer_list = item["answer_list"]
                for index, answer in enumerate(answer_list):
                    code = answer['code']
                    if code == None or code == "":
                        continue
                    with open(self.file_path, "w", encoding="utf8") as file:
                        file.write(code)
                        file.write("\n")
                        file.write(test_code)
                        file.write("\n")
                        file.flush()
                    stdout, stderr, returncode = self._execute()

                    item["result_return_code"] = returncode
                    item["stderr"] = self._remove_color_codes(stderr)
                    item["stdout"] = self._remove_color_codes(stdout)

                    data_list.append(item)
            except Exception as e:
                print(e)
                continue
        data = pd.DataFrame(data_list)
        data.to_excel(f"../analysis/model_answer_result/{self.model_name}/{self.model_name}_typescript.xlsx")

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
            stdout, stderr = process.communicate(timeout=10)
            print(stdout)
            print(stderr)
            print("Process completed with return code:", process.returncode)
            return stdout, stderr, process.returncode
        except subprocess.TimeoutExpired:
            print("Process is being killed after timeout")
            process.kill()
            # 读取任何进程可能产生的输出
            stdout, stderr = process.communicate()
            return stdout, stderr, process.returncode

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
        command = rf"{driver_flag} && cd {driver_flag}\code\python_project\RealisticEval\RealisticEval-Data\envs\typescript && npm run test-silent"
        return command


if __name__ == '__main__':
    typescript_executor = TypeScriptExecutor(model_name="chatglm-6b")
    typescript_executor.batch_run(r"E:\code\code_back\python_project\llm\qa\chatglm-6b_answer\typescript_answer.json")
