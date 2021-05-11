from discord.ext import commands

class General(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def ping(self,ctx):
    await ctx.send(f'Pong! {int(self.bot.latency*1000)}ms')
  

#import commands from main.py or make an event manager cog