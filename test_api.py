from llm import ask_llm

response = ask_llm([
    {
        "role": "user",
         "content":"say hello in one sentence"
    }
])
print(response.content)