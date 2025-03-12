import json


def read_jsonl_data(file_path: str) -> list:
    data_list = []
    with open(file_path, "r", encoding="utf8") as jsonl_file:
        jsonl_data = [line.strip() for line in jsonl_file.readlines()]
    for jd in jsonl_data:
        data = json.loads(jd)
        data_list.append(data)
    return data_list


file_list = ["RealisticCodeBench_python.jsonl", "./RealisticCodeBench_javascript.jsonl",
             "./RealisticCodeBench_typescript.jsonl", "./RealisticCodeBench_c&cpp.jsonl",
             "./RealisticCodeBench_java.jsonl"]

total_data = []
for file in file_list:
    total_data.extend(read_jsonl_data(file))

with open("all_question.json", "w", encoding="utf8") as file:
    json.dump(total_data, file)
