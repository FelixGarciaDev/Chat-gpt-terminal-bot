import openai
import config

openai.api_key = config.api_key

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=[{"role":"user", "content":"¿Cual es la mision de OpenAI?"}])

print(response)
print(response.choices[0].message.content)