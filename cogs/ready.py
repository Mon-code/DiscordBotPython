import discord
from discord.ext import commands
from discord.ext.commands import command
from discord.ext.commands import Cog

class ready(Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.client.get_channel(827842526630903859)
        await channel.connect()

        await self.client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name='niggas'))
        print('Bot has connected to Discord as {0.user}'.format(self.client))

def setup(client):
    client.add_cog(ready(client))