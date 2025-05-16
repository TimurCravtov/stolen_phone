from groq import Groq

# Initialize the client with your API key
client = Groq(api_key="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")

# Make a chat completion request
response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    temperature=0.7,
)

print("Assistant:", response.choices[0].message.content)
