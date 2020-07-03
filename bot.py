import discord
import os
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = Bot(command_prefix='rb!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected!')

bot.run(TOKEN)