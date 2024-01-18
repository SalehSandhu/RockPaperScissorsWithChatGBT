from openai import OpenAI

client = OpenAI(
    api_key= open("API_KEY.txt", "r").read()
)

def insult():

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "insult me for being bad at rock paper scissors\n",
        }
    ],
    model="gpt-3.5-turbo",
    )

    return(chat_completion.choices[0].message.content)