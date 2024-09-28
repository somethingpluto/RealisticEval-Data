import json
import os
import subprocess

import pandas as pd
from tqdm import tqdm

CCPP_RUN_ENV = "../envs/c&cpp"


class CCPPExecutor:
    def __init__(self, model_name=""):
        self._env_path = CCPP_RUN_ENV
        self.model_name = model_name

    def single_run(self, code, test_code):
        with open(f"{self._env_path}/solution.cpp", "w", encoding="utf8") as temp_file:
            temp_file.write(code)
            temp_file.flush()

        with open(f"{self._env_path}/answer_check.cpp", "w", encoding="utf8") as file:
            file.write("#define CATCH_CONFIG_MAIN\n")
            file.write("#include \"./lib/catch.hpp\"\n")
            file.write("#include \"./solution.cpp\"\n")
            file.write(test_code)
            file.flush()
            self._execute()

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
                    with open(f"{self._env_path}/solution.cpp", "w", encoding="utf8") as temp_file:
                        temp_file.write(code)
                        temp_file.flush()
                    with open(f"{self._env_path}/answer_check.cpp", "w", encoding="utf8") as file:
                        file.write("#define CATCH_CONFIG_MAIN\n")
                        file.write("#include \"./lib/catch.hpp\"\n")
                        file.write("#include \"./solution.cpp\"\n")
                        file.write(test_code)
                        file.flush()
                    stdout, stderr, returncode = self._execute()

                    item["result_return_code"] = returncode
                    item["stderr"] = stderr
                    item["stdout"] = stdout

                    data_list.append(item)
            except Exception as e:
                print(e)
                continue
        data = pd.DataFrame(data_list)
        data.to_excel(f"../analysis/model_answer_result/{self.model_name}/{self.model_name}_c&cpp.xlsx")

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
            stdout, stderr = process.communicate(timeout=25)
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

    def _get_file_disk_flag(self):
        # 获取当前文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 分离盘符和路径
        drive_letter = os.path.splitdrive(current_file_path)[0]
        return drive_letter

    def _generate_command(self):
        driver_flag = self._get_file_disk_flag()
        # TODO：替换为 本机中 /code/python_project/RealisticEval-Data/envs 文件中的路径 不必填写盘符
        command = rf'{driver_flag} && cd /code/code_back/python_project/RealisticEval-Data/envs && cd "c&cpp" && g++ -std=c++17 answer_check.cpp -o answer_check && answer_check.exe'
        return command


if __name__ == '__main__':
    code = "\nvoid shellSort(std::vector<int>& arr) {\n    int n = arr.size();\n    for (int i = 0; i < n - 1; i++) {\n        for (int j = 0; j < n - i - 1; j++) {\n            if (arr[j] > arr[j + 1]) {\n                int temp = arr[j];\n                arr[j] = arr[j + 1];\n                arr[j + 1] = temp;\n            }\n        }\n    }\n}\n"
    test_code = "\nbool isSorted(const std::vector<int>& arr) {\n    for (size_t i = 1; i < arr.size(); ++i) {\n        if (arr[i] < arr[i - 1]) {\n            return false;\n        }\n    }\n    return true;\n}\n\nTEST_CASE(\"Shell sort - Basic functionality\", \"[shellSort]\") {\n    SECTION(\"Test Case 1: Already sorted array\") {\n        std::vector<int> arr = {1, 2, 3, 4, 5};\n        shellSort(arr);\n        REQUIRE(isSorted(arr) == true);\n    }\n\n    SECTION(\"Test Case 2: Reverse sorted array\") {\n        std::vector<int> arr = {5, 4, 3, 2, 1};\n        shellSort(arr);\n        REQUIRE(isSorted(arr) == true);\n    }\n\n    SECTION(\"Test Case 3: Array with duplicate elements\") {\n        std::vector<int> arr = {4, 2, 2, 4, 1};\n        shellSort(arr);\n        REQUIRE(isSorted(arr) == true);\n    }\n\n    SECTION(\"Test Case 4: Array with negative numbers\") {\n        std::vector<int> arr = {-3, -1, -4, -2, 0};\n        shellSort(arr);\n        REQUIRE(isSorted(arr) == true);\n    }\n\n    SECTION(\"Test Case 5: Empty array\") {\n        std::vector<int> arr = {};\n        shellSort(arr);\n        REQUIRE(isSorted(arr) == true);\n    }\n}"
    ccpp_executor = CCPPExecutor("test")
    ccpp_executor.single_run(code, test_code)
