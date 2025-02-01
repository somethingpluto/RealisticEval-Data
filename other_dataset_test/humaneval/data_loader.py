import json


def human_eval_data_with_answer_load(file_path: str) ->list:
    data_list = []
    with open(file_path, "r", encoding="utf8") as file:
        jsonl_list = [x.strip() for x in file.readlines()]
    for jsonl in jsonl_list:
        jsonl_data = json.loads(jsonl)
        data_list.append(jsonl_data)

    return data_list



if __name__ == '__main__':
    human_eval_data_with_answer_load("E:\code\code_back\python_project\llm\qa\humaneval\codegeex4-all-9b_answer\python_answer.jsonl")