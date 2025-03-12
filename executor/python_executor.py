import argparse
import glob
import json
import time
from pathlib import Path
import pandas as pd
import subprocess
from tqdm import tqdm

from executor.utils import delete_non_python_and_ipynb_files

PYTHON_RUN_ENV = "../envs/python/qa_item"


class PythonExecutor:
    def __init__(self, model_name, type):
        self._env_path = PYTHON_RUN_ENV
        self.model_name = model_name
        self.type = type
        self.language = "python"
        self.base_path = None
        self.answer_file_path = self._generate_file_path()

    def _generate_file_path(self):
        return rf"E:\code\code_back\python_project\llm\qa\model_answer\{self.model_name}_answer\{self.language}_answer_{self.type}.jsonl"

    def single_run(self, code, test_code):
        with open(f"{self._env_path}/qa_item.py", "w", encoding="utf8") as file:
            file.write(code)
            file.write("\n")
            file.write(test_code)
            file.write("\n")
            file.write("if __name__ == '__main__':")
            file.write("\n")
            file.write("    unittest.main()")
            file.flush()
            self._execute(f"{self._env_path}/qa_item.py")

    def _batch_generate(self):
        result_list = []
        self.base_path = Path(f"{PYTHON_RUN_ENV}/{self.model_name}")
        self.base_path.mkdir(exist_ok=True, parents=True)
        with open(self.answer_file_path, "r", encoding="utf8") as file:
            json_lines = [line.strip() for line in file.readlines()]
            for item in json_lines:
                result_list.append(json.loads(item))
        for item in tqdm(result_list):
            try:
                task_id = item["task_id"]
                print(task_id)
                language_item = item['language_version_list']["python"]
                answer_list = language_item["answer_list"]
                test_code = language_item["test_code"]
                addition_info = language_item["addition_info"]
                for index, answer in enumerate(answer_list):
                    code = answer['response_code']
                    if code == None or code == "":
                        continue
                    with open(f"{self.base_path}/{item['task_id']}_{index}.py", "w", encoding="utf8") as file:
                        file.write(code)
                        file.write("\n")
                        if addition_info != "":
                            file.write(addition_info)
                        file.write(test_code)
                        file.write("\n")
                        file.write("if __name__ == '__main__':")
                        file.write("\n")
                        file.write("    unittest.main()")
                        file.flush()
            except Exception as e:
                print(e)
                continue

    def batch_run(self):
        self._batch_generate()
        result_list = []
        file_list = glob.glob(f"{self.base_path}/**/*.py", recursive=True)
        for file_path in file_list:
            temp = {}
            command = rf"D:\sdk\python\venvs\realisticeval\Scripts\python.exe {file_path}"
            task_id = file_path.split("\\")[-1].split("_")[0]
            print(f"run_test:{task_id}")
            temp["task_id"] = task_id
            try:
                stdout, stderr, return_code = self._execute(command)
            except Exception as e:
                return_code = 1
            temp["result_return_code"] = return_code
            temp["model"] = self.model_name
            result_list.append(temp)
        Path(f"../model_answer_new/{self.model_name}").mkdir(parents=True, exist_ok=True)
        pd.DataFrame(result_list).to_csv(
            f"../model_answer/{self.model_name}/{self.type}/{self.model_name}_{self.language}_{self.type}.csv")

    def _execute(self, command):
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
            try:
                return_code = process.returncode
            except Exception as e:
                return_code = 1
            print("Process completed with return code:", process.returncode)
            process.kill()
            return stdout, stderr, return_code
        except subprocess.TimeoutExpired:
            print("Process is being killed after timeout")
            process.kill()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, help="model_name", required=True)
    parser.add_argument("--type", type=str, help="type pass1 or pass10", required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    executor = PythonExecutor(args.model_name, args.type)
    executor.batch_run()
    time.sleep(4)
    delete_non_python_and_ipynb_files("./")
