from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

user_richard = "jovialime"
user_lindor = "ylw311"

client = OpenAI(api_key = OPENAI_API_KEY)

def get_chatbot_response(user_message):
    content = "You are a helpful assistant named Lindor Bot. The conversation setting is a discord server, so reply casually like it's a text message."
    
    # if user_message.startswith(user_richard):
    #     content += "Reply in a tone scoffing and looking down on the person."
    #     print(f"It's Ririe")
    #     user_message.replace(user_richard, "", 1)

    if user_message.startswith(user_lindor):
        content += "Reply in a sweet and loving tone and always end with the emoji 🌹"
        print(f"It's Lindor")
        user_message.replace(user_lindor, "", 1)

    try:

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": content},
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        print(f"Error fetching OpenAI response: {e}")
        return "Sorry, I couldn't think of a reply. 😅"
