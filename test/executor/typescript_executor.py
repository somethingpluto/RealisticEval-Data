import json
import subprocess

import pandas as pd
from tqdm import tqdm

from test.executor import config


class TypeScriptExecutor:
    def __init__(self, model_name):
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
        result = self._execute(self.file_path)
        print(result.stdout)
        if result.stderr:
            print("error：", result.stderr)
        if result.returncode == 0:
            print("success")
        else:
            print("error return code：", result.returncode)

    def batch_run(self, file_path):
        data_list = []
        with open(file_path, "r", encoding="utf8") as file:
            result_list = json.load(file)

        for item in tqdm(result_list):
            try:
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
                    result = self._execute(self.file_path)

                    item["result_return_code"] = result.returncode
                    item["stderr"] = result.stderr + ""
                    item["stdout"] = result.stdout + ""

                    data_list.append(item)
            except Exception as e:
                print(e)
                continue
        data = pd.DataFrame(data_list)
        data.to_csv(f"../result/{self.model_name}_typescript.csv")

    def _execute(self, file_path):
        command = r"E: && cd E:\code\code_back\python_project\RealisticEval\RealisticEval-Data\envs\typescript && npm run test-silent"
        result = subprocess.run(command, capture_output=True, text=True, timeout=10, shell=True, encoding="utf8")
        return result


if __name__ == '__main__':
    typescript_executor = TypeScriptExecutor(model_name="chatglm-6b")
    typescript_executor.batch_run(r"E:\code\code_back\python_project\llm\qa\chatglm-6b_answer\typescript_answer.json")
