import os


from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()



client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)
MODEL = os.getenv("MODEL")


def ask_llm(messages,tools=None):

    response = client.chat.completions.create(
        model = MODEL,
        messages =messages,
        tools=tools if tools else None,
        tool_choice = "auto" if tools else None,
        temperature = 0.2
    )
    return response.choices[0].message
    



