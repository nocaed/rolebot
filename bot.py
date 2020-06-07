import discord
import os
from dotenv import load_dotenv

# load in the discord client
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
# run the client
client.run(TOKEN)