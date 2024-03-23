from openai import OpenAI

client = OpenAI(api_key="[YOUR_API_KEY]")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo", 
  messages=[
    {"role": "user", "content": "Can you tell me 5 countries in Latin America?"}
  ],
  max_tokens=30
)

print(completion.choices[0].message.content)