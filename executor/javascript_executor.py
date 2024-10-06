import json
import os
import re
import subprocess
import time

import pandas as pd
from tqdm import tqdm

JAVASCRIPT_RUN_ENV = "../envs/javascript"


class JavaScriptExecutor:
    def __init__(self, model_name=""):
        self._env_path = JAVASCRIPT_RUN_ENV
        self.model_name = model_name
        self.file_path = f"{self._env_path}/test.test.js"

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
                    with open(f"{self._env_path}/test.test.js", "r", encoding="utf8") as f:
                        item["full_content"] = f.read()
                    data_list.append(item)
            except Exception as e:
                print(e)
                continue
        data = pd.DataFrame(data_list)
        data.to_excel(f"../analysis/model_answer_result/{self.model_name}/{self.model_name}_javascript.xlsx",
                      engine='xlsxwriter')

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
        # TODO: 替换为 本机中 RealisticEval-Data\envs\javascript 文件中的路径 不必填写盘符
        command = f"{driver_flag} && cd {driver_flag}/code/code_back/python_project/RealisticEval-Data/envs/javascript && npm run test-silent"
        return command


if __name__ == '__main__':
    code = "\nfunction getPrice(recipeId, minVal = 10, maxVal = 30) {\n  let price = 0;\n  let hash = recipeId.toString(36).padStart(32, '0');\n  for (let i = 0; i < minVal; i++) {\n    hash = hash.substring(0, 8) + Math.floor(hash / 10) * (maxVal - i) + hash.substring(8);\n  }\n  return Math.round(price * 100 / 10) / 10;\n}\n"
    test_code = "describe('getPrice', () => {\n    test('should return a number within the default range for a given recipe ID', () => {\n        const price = getPrice('recipe123');\n        expect(price).toBeGreaterThanOrEqual(10);\n        expect(price).toBeLessThanOrEqual(30);\n    });\n\n    test('should return the same price for the same recipe ID', () => {\n        const price1 = getPrice('recipe123');\n        const price2 = getPrice('recipe123');\n        expect(price1).toBe(price2);\n    });\n\n    test('should return different prices for different recipe IDs', () => {\n        const price1 = getPrice('recipe123');\n        const price2 = getPrice('recipe456');\n        expect(price1).not.toBe(price2);\n    });\n\n    test('should return a price within a custom range', () => {\n        const minVal = 20;\n        const maxVal = 50;\n        const price = getPrice('recipe789', minVal, maxVal);\n        expect(price).toBeGreaterThanOrEqual(minVal);\n        expect(price).toBeLessThanOrEqual(maxVal);\n    });\n\n    test('should handle very long recipe IDs without error', () => {\n        const longRecipeId = 'recipe' + 'A'.repeat(1000);\n        const price = getPrice(longRecipeId);\n        expect(price).toBeGreaterThanOrEqual(10);\n        expect(price).toBeLessThanOrEqual(30);\n    });\n});"
    javascript_executor = JavaScriptExecutor(model_name="chatglm-6b")
    javascript_executor.single_run(code, test_code)
    # javascript_executor.batch_run(
    #     "E:\code\code_back\python_project\llm\qa\chatglm-6b_answer\javascript_answer.json")
