import discord
from typing import Optional
from discord.ext import commands
from discord import Embed, Member
from discord.ext.commands import Cog

class avatar(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='avatar', aliases=['av'])
    async def avatar(self, ctx, target: Optional[Member]):
        target = target or ctx.author

        embed = Embed(title=f"{target}'s Avatar", colour=target.colour)

        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_image(url=target.avatar_url)
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(avatar(client))