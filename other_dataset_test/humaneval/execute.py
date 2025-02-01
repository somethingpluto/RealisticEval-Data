import glob
import os
import subprocess
from pathlib import Path

import pandas as pd

from other_dataset_test.humaneval.data_loader import human_eval_data_with_answer_load


def make_all_tes_file(data_list: list):
    for data in data_list:
        task_id = data["task_id"].replace("/", "_")
        test = data["test"]
        answer_list = data["answer_list"]
        func_name = data["entry_point"]
        for answer in answer_list:
            try:
                index = answer["index"]
                response_code = answer["response_code"]
                file_path = f"./test/{task_id}_{index}.py"
                test_file_path = Path(file_path)
                if not test_file_path.exists():
                    test_file_path.touch(exist_ok=True)
                with open(test_file_path, "w", encoding="utf8") as test_file:
                    test_file.write(test)
                    test_file.write(response_code)
                    test_file.write("\n")
                    test_file.write(f"candidate = {func_name}\n")
                    test_file.write("check(candidate)")
            except Exception as e:
                print(e)
                continue


def execute(test_file_dir: str, task: dict):
    result_list = []
    file_list = glob.glob(f"{test_file_dir}/**/*.py", recursive=True)
    for file in file_list:
        try:
            temp_result = {}
            command = rf"D:\sdk\python\venvs\RealisticEval-Data\Scripts\python.exe {file}"
            stdout, stderr, code = command_execute(command)
            temp_result["file"] = file.split("\\")[-1]
            temp_result["stdout"] = stdout
            temp_result["stderr"] = stderr
            temp_result["return_code"] = code
            print(f"{file} {code}")
            result_list.append(temp_result)
        except Exception as e:
            temp_result["stderr"] = f"{e}"
            result_list.append(temp_result)
    pd.DataFrame(result_list).to_excel(f"./result/{task['model']}_{task['type']}.xlsx", index=False)
    clear_test_env(test_file_dir)


def clear_test_env(test_file_dir: str):
    file_list = glob.glob(f"{test_file_dir}/**/*.py", recursive=True)
    for file in file_list:
        os.remove(file)


def command_execute(command: str):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout, result.stderr, result.returncode


if __name__ == '__main__':
    task_list = [
        # {
        #     "model": "codegeex4-all-9b_answer",
        #     "type": "pass1"
        # },
        # {
        #     "model": "codegeex4-all-9b_answer",
        #     "type": "pass10"
        # },
        {
            "model": "deepseek-coder-6.7b-instruct",
            "type": "pass1"
        },
        {
            "model": "deepseek-coder-6.7b-instruct",
            "type": "pass10"
        },
    ]

    for task in task_list:
        data_list = human_eval_data_with_answer_load(
            f"E:\code\code_back\python_project\llm\qa\humaneval\\{task['model']}_answer\python_answer_{task['type']}.jsonl")
        make_all_tes_file(data_list=data_list)
        execute("./test", task)
