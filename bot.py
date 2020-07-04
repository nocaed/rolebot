import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

# load in bot token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# initialize bot
bot = Bot(command_prefix='rb!')

# checks if role exists
def check_role_existence(target, roles):
    for role in roles:
        if role.name == target:
            return True
    return False

# send connection notification when bot is ready for use
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected!')

# adds a role to the server the bot is on
@bot.command(name='add', help='Adds a new, non-restricted role with the same rights as @everyone')
#@commands.has_role('Admin')
async def add(ctx, role_name: str):
    guild = ctx.guild
    found = check_role_existence(role_name, guild.roles)

    if found:
        await ctx.send(f'Role {role_name} already exists in this server.')
    else:
        await guild.create_role(name=role_name)
        await ctx.send(f'Role {role_name} has been created.')

# run the bot
bot.run(TOKEN)