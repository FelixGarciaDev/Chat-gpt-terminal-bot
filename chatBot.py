import openai
import config

openai.api_key = config.api_key

# Contexto de nuestro aplicación
context =  [{
    "role": "system",
    "content": "Eres un traductor muy util"
}]

messages = context

while True:
    content = input("dime o preguntame lo que quieras:")

    if content == "exit":
        break
    messages.append({"role":"user", "content": content})

    response_raw = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                temperature=0.9,                                               
                                                messages=messages)
    
    response_content = response_raw.choices[0].message.content

    messages.append({"role":"assistant", "content": response_content})

    print(response_content)
    print("==="*15)
    print("\n")