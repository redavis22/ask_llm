from openai import OpenAI
key = " insert key here"
client = OpenAI(api_key=key)

prompt = input('Ask LLM: ' + '\n')

client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)



response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    "role": "system", "content": "GIVE ONE LINE BASH COMMAND AS YOUR ANSWER. BASH FORMAT ONLY",
    "role": "user", "content": prompt
  ],
  max_tokens=300,
)

print("\n Answer is: \n")
print(response.choices[0].message.content)
print("\n")
