from openai import OpenAI

import json
from tqdm import tqdm


def extract_code_from_content(language, content):
    start = content.find("```")
    if start == -1:
        return content

    end = content.find("```", start + 3)
    if end == -1:
        return content

    code_block = content[start + 3:end].strip()

    first_newline = code_block.find("\n")
    if first_newline != -1:
        # 如果找到换行符，说明有语言标记，去掉这一行
        code_block = code_block[first_newline:].strip()
    if language != "c&cpp":
        return code_block
    elif language == "c&cpp":
        return code_block.split("int main()")[0]
    return code_block


def call_with_message(temperature, num_of_sequence, messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature,
        max_tokens=4096,
        n=num_of_sequence
    )
    return response


client = OpenAI(
    api_key="sk-zk2af6da35eeba0728a4e4ded82f5a66144660282e42e179",
    base_url="https://flag.smarttrot.com/v1/"
)

if __name__ == '__main__':
    LANGUAGE_LIST = ["java"]
    QUESTION_PATH = r"E:\code\code_back\python_project\llm\qa\question\all_question.json"
    PASS_NUMBER = 1
    temperature = 0
    num_of_sequence = 1
    if PASS_NUMBER == 1:
        temperature = 0
        num_of_sequence = 1
    elif PASS_NUMBER == 10:
        temperature = 0.8
        num_of_sequence = 10
    MODEL_NAME = "gpt-4"
    ANSWER_PATH = rf"E:\code\code_back\python_project\llm\qa\{MODEL_NAME}_answer"
    for language in LANGUAGE_LIST:
        with open(QUESTION_PATH, "r", encoding="utf8") as file:
            question_list = json.load(file)
            for question in tqdm(question_list):
                all_response = []
                try:
                    prompt = question["language_version_list"][language]['prompt']
                    if prompt == "":
                        continue
                    messages = [
                        {'role': 'user',
                         'content': prompt + ".give me all function/class code, no examples are required."}
                    ]
                    response = call_with_message(temperature, num_of_sequence, messages)
                    for idx, choice in enumerate(response.choices, 1):
                        all_response.append({"index": idx, "model_name": MODEL_NAME,
                                             "response_code": extract_code_from_content(language,
                                                                                        choice.message.content)})
                        print(extract_code_from_content(language, choice.message.content))
                    question["language_version_list"][language]["answer_list"] = all_response
                    with open(f"{ANSWER_PATH}/{language}_answer_pass{PASS_NUMBER}.jsonl", "a+",
                              encoding='utf8') as file:
                        json_str = json.dumps(question)
                        file.write(json_str + "\n")
                        file.flush()
                except Exception as e:
                    print(e)
                    continue
                print(f"{question['task_id']} start answer finish")
