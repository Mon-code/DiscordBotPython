import discord
from discord.ext import commands
from discord.ext.commands import Cog

class pause_resume(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()

def setup(client):
    client.add_cog(pause_resume(client))