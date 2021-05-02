import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix= "!")
path = r"\Users\Faiq Haidar\Documents\FAIQ\Coding\Python\bot\cogs"
dir = os.listdir(path)

for file in dir:
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')

client.run('NzY5NTMxNDk5OTQ2NDQyODEy.X5QYDg._ApGLNBICeIxlo32a1JVtxf0PWU')