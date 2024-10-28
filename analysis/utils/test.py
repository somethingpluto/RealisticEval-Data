import openai

# 设置 OpenAI API 密钥和自定义 API 基础 URL
openai.api_key = "sk-zk2af6da35eeba0728a4e4ded82f5a66144660282e42e179"
openai.api_base = "https://flag.smarttrot.com/v1/"  # 设置自定义 base_url

def classify_requirement(requirement_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "你是一个软件需求分类助手，分类为功能性需求或非功能性需求，并指定非功能性需求的类别。"},
                {"role": "user", "content": f"需求: {requirement_text} 请进行分类。"}
            ]
        )
        # 获取 GPT-3.5 的分类结果
        classification = response['choices'][0]['message']['content'].strip()
        return classification

    except Exception as e:
        return f"调用GPT-3.5失败: {e}"

if __name__ == '__main__':
    print(classify_requirement("编写一个快速排序"))