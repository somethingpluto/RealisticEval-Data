import json
import subprocess

import pandas as pd
from tqdm import tqdm

from test.executor import config


class JavaScriptExecutor:
    def __init__(self, model_name):
        self._env_path = config.JAVASCRIPT_RUN_ENV
        self.model_name = model_name
        self.file_path = f"{self._env_path}/test.test.js"

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
        data.to_csv(f"../result/{self.model_name}_javascript.csv")

    def _execute(self, file_path):
        command = "E: && cd E:\code\code_back\python_project\RealisticEval\RealisticEval-Data\envs\javascript && npm run test-silent"
        result = subprocess.run(command, capture_output=True, text=True, timeout=10, shell=True, encoding="utf8")
        return result


if __name__ == '__main__':
    code = "function timestampToReadableDate(unixTimestamp) {\n    const date = new Date(unixTimestamp * 1000);\n    const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];\n    const days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];\n    const readableDate = `${days[date.getDay()]} ${date.getDate()} ${months[date.getMonth()]}, ${date.getHours()}:${date.getMinutes() < 10 ? '0' : ''}${date.getMinutes()}`;\n    return readableDate;\n}"
    test_code = "describe('timestampToReadableDate', () => {\n    test('converts Unix timestamp for New Year\\'s Day', () => {\n        // January 1, 2023 00:00 GMT\n        expect(timestampToReadableDate(1672531200)).toBe('Jan 1, 8:00');\n    });\n\n    test('converts Unix timestamp for a leap day', () => {\n        // February 29, 2024 12:00 GMT (leap year)\n        expect(timestampToReadableDate(1709227200)).toBe('Mar 1, 1:20');\n    });\n\n    test('converts Unix timestamp for a summer day', () => {\n        // June 21, 2023 15:45 GMT\n        expect(timestampToReadableDate(1687362300)).toBe('Jun 21, 23:45');\n    });\n\n    test('handles minutes with leading zero', () => {\n        // October 3, 2023 02:05 GMT\n        expect(timestampToReadableDate(1696377900)).toBe('Oct 4, 8:05');\n    });\n\n    test('handles end of the year', () => {\n        // December 31, 2023 23:59 GMT\n        expect(timestampToReadableDate(1704067140)).toBe('Jan 1, 7:59');\n    });\n});"
    javascript_executor = JavaScriptExecutor(model_name="chatglm-6b")
    # javascript_executor.single_run(code, test_code)
    javascript_executor.batch_run(
        "E:\code\code_back\python_project\llm\qa\chatglm-6b_answer\javascript_answer.json")
