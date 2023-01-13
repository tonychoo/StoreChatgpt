import openai

# Use your OpenAI API key
openai.api_key = "{APIKey}"

# The message you want to send to ChatGPT
message = "{Message}"

# Send the message to ChatGPT and receive the response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=message,
    max_tokens=2048,
    n = 1,
    stop=None,
    temperature=0.5
)

# Extract the ChatGPT's response from the JSON object
chatgpt_response = response["choices"][0]["text"].strip()

print(chatgpt_response)
