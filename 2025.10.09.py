# 我国的义务教育阶段为什么要将信息技术学科改名为信息科技?
# sk-be17413ed52f4f88b1f27076f7890ce9

# Please install OpenAI SDK first: `pip3 install openai`
from openai import OpenAI

client = OpenAI(
    api_key="sk-be17413ed52f4f88b1f27076f7890ce9",
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个ai助手，请你回答用户的问题，并且回答时使用普通文本格式，不需要加入markdown语法"},
        {"role": "user", "content": "我国的义务教育阶段为什么要将信息技术学科改名为信息科技?"},
    ],
    stream=False,
    max_tokens=256
)

print(response.choices[0].message.content)
