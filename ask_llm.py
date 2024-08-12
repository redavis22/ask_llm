from openai import OpenAI
key = " insert key here"
client = OpenAI(api_key=key)

prompt = input('Ask LLM: ' + '\n')

client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)


while(True):
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": prompt},
            # {
            #   "type": "image_url",
            #   "image_url": {
            #     "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            #   },
            # },
          ],
        }
      ],
      max_tokens=300,
    )
    
    print(response.choices[0].message.content)
