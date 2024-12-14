import discord
import os
from dotenv import load_dotenv
from chatbot import get_chatbot_response

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
TARGET_USER_ID = int(os.getenv('TARGET_USER_ID'))
DEVELOPER_NAME = os.getenv('DEVELOPER_NAME')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "cute" in message.content:
        await message.channel.send('awww 🌹')

    if "lindor" in message.content:
        await message.channel.send('angel loves lindor 🌹')

    # if message.author.name == DEVELOPER_NAME:
    #     print(f'Im angel hehe')

    if message.author.id == TARGET_USER_ID:
        await message.add_reaction('🌹')

    if message.author.name == 'jovialime':
        await message.add_reaction('👎')
        await message.add_reaction('💀')

    if message.content.startswith('$question'):
        openai_response = get_chatbot_response(message.author.name + message.content)
        await message.channel.send(openai_response)

client.run(DISCORD_BOT_TOKEN)

