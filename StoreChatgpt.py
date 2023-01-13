import openai

# Use your OpenAI API key
openai.api_key = "{APIKey}"

while True:
    message = input("You: ")
    if message.lower() == "exit":
        break
    # Send the message to ChatGPT and receive the response
    try:
        response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=message,
                max_tokens=2048,
                n = 1,
                stop=None,
                temperature=0.5,
                timeout=10
            )
        # Extract the ChatGPT's response from the JSON object
        chatgpt_response = response["choices"][0]["text"].strip()
        print("ChatGPT: " + chatgpt_response)
    except openai.exceptions.OpenAiError as e:
        print("Error: ", e)
        break

    print("ChatGPT: " + chatgpt_response)
