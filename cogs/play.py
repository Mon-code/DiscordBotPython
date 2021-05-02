import discord
import os
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Cog

class play(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, url : str):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            return

        if ctx.message.author.voice:
            channel = ctx.message.author.voice.channel
            await channel.connect()

        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))

def setup(client):
    client.add_cog(play(client))
