import argparse
import glob
import os.path
import subprocess
from pathlib import Path

import pandas as pd

from other_dataset_test.humaneval.data_loader import human_eval_data_with_answer_load


def make_all_tes_file(model_name: str, data_list: list):
    """生成所有的python 文件

    Args:
        data_list (list):
    """
    # 创建对应的文件夹
    dir_path = f"./test/{model_name}"
    Path(dir_path).mkdir(exist_ok=True, parents=True)
    for task_id, data in enumerate(data_list):
        test = data["test"]
        answer_list = data["answer_list"]
        func_name = data["entry_point"]
        for answer in answer_list:
            try:
                index = answer["index"]
                response_code = answer["response_code"]
                file_path = f"./test/{model_name}/{task_id}_{index}.py"
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


def execute(test_file_dir: str, model_name: str, type: str):
    result_list = []
    file_list = glob.glob(f"{test_file_dir}/**/*.py", recursive=True)
    for file in file_list:
        try:
            temp_result = {}
            command = rf"D:\sdk\python\venvs\RealisticEval-Data\Scripts\python.exe {file}"
            stdout, stderr, code = command_execute(command)
            file_info = file.split("\\")[-1].split("_")
            temp_result["task_id"] = file_info[0]
            temp_result["index"] = file_info[1].replace(".py", "")
            temp_result["stdout"] = stdout
            temp_result["stderr"] = stderr
            temp_result["return_code"] = code
            print(f"{file} {code}")
            result_list.append(temp_result)
        except Exception as e:
            temp_result["stderr"] = f"{e}"
            result_list.append(temp_result)
    pd.DataFrame(result_list).sort_values(by='task_id').to_excel(f"./result/{model_name}_{type}.xlsx", index=False)


def command_execute(command: str):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout, result.stderr, result.returncode


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, help="model name", required=True)
    parser.add_argument("--type", type=str, help="use which gpu", required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    base_file = "E:\code\code_back\python_project\llm\qa\other_benchmark\humaneval"
    result_data_path = os.path.join(base_file, f"{args.model_name}_answer", f"python_answer_{args.type}.jsonl")
    data = human_eval_data_with_answer_load(result_data_path)
    make_all_tes_file(args.model_name, data)
    execute(f"./test/{args.model_name}", args.model_name, args.type)
