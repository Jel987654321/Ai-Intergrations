import openai

# Replace with your OpenAI API key
api_key = 'your_openai_api_key'
openai.api_key = api_key

# Example prompt for GPT-3 model
prompt = "Translate the following text into French: 'Hello, how are you?'"

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=50
)

print(response.choices[0].text.strip())
