import discord
from typing import Optional
from discord.ext import commands
from discord.ext.commands import Cog

class clear(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount : Optional[int]):
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(clear(client))