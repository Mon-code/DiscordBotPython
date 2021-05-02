from datetime import datetime
from typing import Optional
from discord.ext import commands
from discord import Embed, Member
from discord.ext.commands import Cog
from discord.ext.commands import command

class userinfo(Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name="userinfo", aliases=["uinfo", "ui"])
	async def user_info(self, ctx, target: Optional[Member]):
		target = target or ctx.author

		embed = Embed(colour=target.colour)

		embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
		embed.set_thumbnail(url=target.avatar_url)

		fields = [("ID", target.id, True),
		          ("Username", str(target), True),
		          ("Mention", target.mention, False),
				  ("Created at", target.created_at.strftime("%A, %B %dth %Y @ %H:%M:%S %p"), True),
				  ("Joined at", target.joined_at.strftime("%A, %B %dth %Y @ %H:%M:%S %p"), False),
				  ("Roles", ', '.join(list(map(lambda x: x.mention, target.roles[::-1]))), False)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(userinfo(client)) 