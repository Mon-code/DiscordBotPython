import discord
from discord.ext import commands

class leave(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def join(self, ctx):
        if ctx.message.author.voice:
            channel = ctx.message.author.voice.channel
            await channel.connect()
            return
        
def setup(client):
    client.add_cog(leave(client))
