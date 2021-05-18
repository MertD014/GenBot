import discord
from discord.ext import commands
import asyncio
import opus
import youtube_dl
import nacl

youtube_dl.utils.bug_reports_message = lambda: ''

queue = []

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
  def __init__(self, source, *, data, volume=0.5):
    super().__init__(source, volume)
    self.data = data
    self.title = data.get('title')
    self.url = data.get('url')

  @classmethod
  async def from_url(cls, url, *, loop=None, stream=False):
    loop = loop or asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

    if 'entries' in data:
      # take first item from a playlist
      data = data['entries'][0]

    filename = data['url'] if stream else ytdl.prepare_filename(data)
    return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


#magic above i literally didint understand a bit



class Music(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def join(self, ctx, *, channel: discord.VoiceChannel):
    if ctx.voice_client is not None:
      return await ctx.voice_client.move_to(channel)
    await channel.connect()

  @commands.command(alias="stop")
  async def leave(self, ctx):
    await ctx.voice_client.disconnect()  #empty queue

  @commands.command()
  async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
      
  @commands.command()
  async def resume(ctx):
      voice_client = ctx.message.guild.voice_client
      if voice_client.is_paused():
          await voice_client.resume()
      else:
          await ctx.send("The bot is not playing anything at the moment.")

  @commands.command()
  async def play(self, ctx, *, url):
    async with ctx.typing():
      player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
      ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.send(f'Now playing: {player.title}')

  @commands.command()
  async def volume(self, ctx, volume: int):
    if ctx.voice_client is None:
      return await ctx.send("Not connected to a voice channel.")
    ctx.voice_client.source.volume = volume / 100
    await ctx.send(f"Changed volume to {volume}%")

  

  @play.before_invoke
  async def ensure_voice(self, ctx):
    if ctx.voice_client is None:
      if ctx.author.voice:
        await ctx.author.voice.channel.connect()
      else:
        await ctx.send("You are not connected to a voice channel.")
        raise commands.CommandError("Author not connected to a voice channel.")
    elif ctx.voice_client.is_playing():
      ctx.voice_client.stop()


  """
  loop
  loop queue
  add queue
  list queue
  skip
  
  """