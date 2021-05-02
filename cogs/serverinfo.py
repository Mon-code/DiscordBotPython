import discord
from datetime import datetime
from typing import Optional
from discord.ext import commands
from discord import Embed, Member
from discord.ext.commands import Cog
from discord.ext.commands import command

class serverinfo(Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name="serverinfo", aliases=["sinfo", "si"])
	async def server_info(self, ctx, guild: discord.Guild = None):
		embed = Embed(colour=0x00ff00)

		embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)

		fields = [("ID", ctx.guild.id, True),
		          ("Region", ctx.guild.region, False),
				  ("Members", ctx.guild.member_count, False),
				  ("Roles", str(len(ctx.guild.roles)), False),
				  ("Created at", ctx.guild.created_at.strftime("%A, %B %dth %Y @ %H:%M:%S %p"), False)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(serverinfo(client))