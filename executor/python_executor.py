import argparse
import json
import os.path

import pandas as pd

import subprocess
from tqdm import tqdm

PYTHON_RUN_ENV = "../envs/python/temp"
def delete_non_python_and_ipynb_files(directory):
    """
    删除指定目录下所有非 Python (.py) 和非 Jupyter Notebook (.ipynb) 文件

    :param directory: 需要检查的目录路径
    """
    # 确保目录存在
    if not os.path.isdir(directory):
        print(f"目录 '{directory}' 不存在。")
        return

    # 遍历目录中的所有文件和子目录
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # 如果是文件且扩展名不是.py或.ipynb，则删除该文件
        if os.path.isfile(file_path) and not (filename.endswith('.py') or filename.endswith('.ipynb')):
            try:
                os.remove(file_path)
                print(f"已删除文件: {file_path}")
            except Exception as e:
                print(f"无法删除文件 {file_path}: {e}")

class PythonExecutor:
    def __init__(self, type, model_name=""):
        self._env_path = PYTHON_RUN_ENV
        self.model_name = model_name
        self.type = type
        self.language = "python"

    def single_run(self, code, test_code):
        with open(f"{self._env_path}/temp.py", "w", encoding="utf8") as file:
            file.write(code)
            file.write("\n")
            file.write(test_code)
            file.write("\n")
            file.write("if __name__ == '__main__':")
            file.write("\n")
            file.write("    unittest.main()")
            file.flush()
            self._execute(f"{self._env_path}/temp.py")

    def batch_run(self, file_path):
        result_list = []
        data_list = []
        with open(file_path, "r", encoding="utf8") as file:
            json_lines = [line.strip() for line in file.readlines()]
            for item in json_lines:
                result_list.append(json.loads(item))

        for item in tqdm(result_list):
            try:
                print(item["task_id"])
                if int(item["task_id"]) not  in [64,72,
79,
215,
224,
230,
231,
233,
240,
290,
291,
406,
412,
413,
414,
420,
478,
488,
490,
495,
513,
523,
550,
555,
557,
95,
96,
106,
108,
112,
115,
120,
127,
130,
139,
292,
306,
326,
450,
528,
529,
532,
535,
536,
540,
545,
142,
583,
179,
180,
612,
614,
625,
626,
628,
631,
633,
190,
192,
193,
198,
200,
205,
361,
592,
599,
603]:
                    continue
                language_item = item['language_version_list']["python"]
                answer_list = language_item["answer_list"]
                test_code = language_item["test_code"]
                addition_info = language_item["addition_info"]
                for index, answer in enumerate(answer_list):
                    code = answer['response_code']
                    if code == None or code == "":
                        continue
                    with open(f"{self._env_path}/temp.py", "w", encoding="utf8") as file:
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
                    stdout, stderr, returncode = self._execute(f"{self._env_path}/temp.py")
                    item["result_return_code"] = returncode
                    item["stderr"] = stderr
                    item["stdout"] = stdout
                    item["answer_index"] = index
                    item["model"] = answer["model_name"]
                    with open(f"{self._env_path}/temp.py", "r", encoding="utf8") as f:
                        item["full_content"] = f.read()
                    data_list.append(item)
                    # xlsx_data_list = item.values()
                    # print(xlsx_data_list)
                    # append_row_to_xlsx(f"../analysis/model_answer_result/{self.model_name}/{self.type}/{self.model_name}_{self.language}_{self.type}.xlsx",xlsx_data_list)
                    # append_row_to_xlsx(rf"C:\Users\pluto\Desktop\temp\{self.model_name}\{self.model_name}_{self.language}_{self.type}.xlsx",xlsx_data_list)
            except Exception as e:
                print(e)
                continue
            delete_non_python_and_ipynb_files("./")
        result_data = pd.DataFrame(data_list)
        result_data.to_excel(f"../analysis/model_answer_result/{self.model_name}/{self.type}/{self.model_name}_{self.language}_{self.type}.xlsx",engine="xlsxwriter")


    def _execute(self, file_path):
        abs_path = os.path.abspath(file_path)
        # TODO: 替换为本机python环境中的python.exe文件路径
        command = rf"D:\sdk\python\venvs\realisticeval\Scripts\python.exe {abs_path}"
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



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, help="model_answer_file_path", required=True)
    parser.add_argument("--type", type=str, help="type pass1 or pass10", required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    executor = PythonExecutor(args.type, args.model_name)
    file_path = rf"E:\code\code_back\python_project\llm\qa\{args.model_name}_answer\python_answer_{args.type}.jsonl"
    executor.batch_run(file_path)
