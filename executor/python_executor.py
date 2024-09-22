import json
import os.path

import pandas as pd

import executor.config as config
import subprocess
from tqdm import tqdm


class PythonExecutor:
    def __init__(self, model_name=""):
        self._env_path = config.PYTHON_RUN_ENV
        self.model_name = model_name

    def single_run(self, code, test_code):
        with open(f"{self._env_path}/temp.py", "w", encoding="utf8") as file:
            file.write(code)
            file.write("\n")
            file.write(test_code)
            file.write("\n")
            file.write("if __name__ == '__main__':")
            file.write("    unittest.main()")
            file.flush()
            self._execute(f"{self._env_path}/temp.py")

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
                    with open(f"{self._env_path}/temp.py", "w", encoding="utf8") as file:
                        file.write(code)
                        file.write("\n")
                        file.write(test_code)
                        file.write("\n")
                        file.write("if __name__ == '__main__':")
                        file.write("    unittest.main()")
                        file.flush()
                    stdout, stderr, returncode = self._execute(f"{self._env_path}/temp.py")
                    item["result_return_code"] = returncode
                    item["stderr"] = stderr
                    item["stdout"] = stdout
                    data_list.append(item)
            except Exception as e:
                print(e)
                continue
        data = pd.DataFrame(data_list)
        data.to_excel(f"../analysis/model_answer_result/{self.model_name}/{self.model_name}_python.xlsx")

    def _execute(self, file_path):
        abs_path = os.path.abspath(file_path)
        command = rf"D:\sdk\python\venvs\realisticeval\Scripts\python.exe {abs_path}"
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
