import requests
import re
import json
from tqdm import tqdm

def extract_code_from_content(language, text):
    pattern = re.compile(r'```(.*?)```', re.DOTALL)

    # Find all content blocks in the text
    content_blocks = pattern.findall(text)

    code_str = "".join(content_blocks)
    if language != "c&cpp":
        return code_str.replace(language, "", 1)
    elif language == "c&cpp":
        code_str = code_str.split("int main()")[0]
        return code_str.replace(language, "", 1)


def send_message(temperature, prompt):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/completions/codellama_7b_instruct?access_token=" + get_access_token()

    payload = json.dumps({
        "prompt": prompt,
        "temperature": temperature,
        "top_p": 0.95
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

API_KEY = "gnNaHBiU9HtdJBtRjvybhIw1"
SECRET_KEY = "aFd9QZo8WgjXhvV7IHMTfBpbkpL0020O"

if __name__ == '__main__':
    LANGUAGE_LIST = ["c&cpp","java"]
    QUESTION_PATH = r"E:\code\code_back\python_project\llm\qa\question\all_question.json"
    PASS_NUMBER = 1
    temperature = 0
    if PASS_NUMBER == 1:
        temperature = 0.01
    elif PASS_NUMBER == 10:
        temperature = 0.8
    MODEL_NAME = "CodeLlama-7b-hf"
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
                    messages = prompt + ".give me all code,no examples are required."
                    for loop in range(1, PASS_NUMBER + 1):
                        response = send_message(temperature, messages)
                        response_code = response['result']
                        print(extract_code_from_content(language,response_code))
                        all_response.append({"index": loop, "model_name": MODEL_NAME, "response_code": extract_code_from_content(language,response_code)})
                    question["language_version_list"][language]["answer_list"] = all_response
                    with open(f"{ANSWER_PATH}/{language}_answer_pass{PASS_NUMBER}.jsonl", "a+", encoding='utf8') as file:
                        json_str = json.dumps(question)
                        file.write(json_str + "\n")
                        file.flush()
                except Exception as e:
                    print(e)
                    continue
                print(f"{question['task_id']} start answer finish")