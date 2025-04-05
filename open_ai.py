from openai import OpenAI

# Set your API key
client=OpenAI(
api_key = "",
)



# Example: Using ChatGPT model
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
      {"role": "system", "content": "You are a virtual assistant named papa like alexa,you give answers for general questions shortly."},
      {"role": "user", "content": "what is coding"}
  ]
)

print(response.choices[0].message)
