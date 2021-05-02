from datetime import datetime
from typing import Optional
from discord.ext import commands
from discord import Embed, Member
from discord.ext.commands import Cog
from discord.ext.commands import command

class help(Cog):
	def __init__(self, client):
		self.client = client
		self.client.remove_command("help")

	@commands.command(name="help", aliases=['h'])
	async def help_commands(self, ctx):
		embed = Embed(colour=0xff0000)

		embed.set_author(name="Help Commands", icon_url=ctx.guild.icon_url)

		tuple = ("> ""`avatar`", "`ping`", "`clear`", "`serverinfo`", "`userinfo`", "\n", "> ""`join/leave`", "`help`", "`icon`")

		fields = [("Prefix:", "> **!**", True),
		          ("Commands:", " ".join(tuple), False)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(help(client))
