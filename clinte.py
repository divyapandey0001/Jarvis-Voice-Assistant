from openai import OpenAI

# Always keep API key secret
client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(response.choices[0].message.content)
