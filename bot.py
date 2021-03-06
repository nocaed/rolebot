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

# required role to use restricted features of this bot
CONTROLLER = 'rb'
restricted_roles = [CONTROLLER, 'Admin']

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
async def add(ctx, role_name: str):
    guild = ctx.guild
    found = check_role_existence(role_name, guild.roles)

    if found:
        await ctx.send(f'Role {role_name} already exists in this server.')
    else:
        await guild.create_role(name=role_name)
        await ctx.send(f'Role {role_name} has been created.')

# adds a role to the server the bot is on
@bot.command(name='remove', help='Removes a role from the server, only users with the "rb" role can use this.')
@commands.has_role(CONTROLLER)
async def remove(ctx, role_name: str):
    guild = ctx.guild
    found = check_role_existence(role_name, guild.roles)

    if found:
        # find a way to remove roles
        # await ctx.message.author.
        await ctx.send(f'Role {role_name} has been deleted.')
    else:
        await ctx.send(f'Role {role_name} does not exist in this server.')

# run the bot
bot.run(TOKEN)