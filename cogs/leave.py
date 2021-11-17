import discord
from discord.ext import commands

class leave(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()

def setup(client):
    client.add_cog(leave(client)) 