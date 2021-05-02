import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix= "!")
path = r"\your directory here"
dir = os.listdir(path)

for file in dir:
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')

client.run('your bot token')
