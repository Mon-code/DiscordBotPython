import discord
from discord.ext import commands
from discord.ext.commands import Cog
from typing import Optional
from discord import Member

class message(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, arg, target: Optional[Member]):
        target = target or ctx.author

        await ctx.channel.purge(limit=1)        
        await ctx.send(arg)

def setup(client):
    client.add_cog(message(client))