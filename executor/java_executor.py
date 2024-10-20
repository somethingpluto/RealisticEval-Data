import json
import os
import re
import subprocess

import pandas as pd
from tqdm import tqdm

JAVA_RUN_ENV = "../envs/java/src"


class JavaExecutor:
    def __init__(self, model_name=""):
        self._env_path = JAVA_RUN_ENV
        self.model_name = model_name

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
        data_list = []
        with open(file_path, "r", encoding="utf8") as file:
            result_list = json.load(file)
        for item in tqdm(result_list):
            try:
                print(item["task_id"])
                test_code = item['test_code']
                addition_info = item["addition_info"]
                answer_list = item["answer_list"]
                for index, answer in enumerate(answer_list):
                    code = answer['code']

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
                    data_list.append(item)
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
            # 读取任何进程可能产生的输出
            stdout, stderr = process.communicate()
            return stdout, stderr, process.returncode

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


if __name__ == '__main__':
    with open("../all/t170/java/Answer.java", "r", encoding="utf8") as code_file:
        code = code_file.read()
    with open("../all/t170/java/Tester.java", "r", encoding="utf8") as test_file:
        test = test_file.read()
    java_executor = JavaExecutor("test")
    java_executor.single_run(code, test)
