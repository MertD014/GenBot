import discord
from discord.ext import commands

prefixes = dict()
defaultPrefix = '.'

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  
  async def getPrefix(self, ctx):
    if ctx.guild.id in prefixes:
      return prefixes.get(ctx.guild.id)
    return defaultPrefix

  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'Pong! {int(self.bot.latency*1000)}ms')

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def setPrefix(self, ctx, newPrefix):
    prefixes[ctx.guild.id] = newPrefix
    await ctx.send(prefixes.get(ctx.guild.id))



    
  
#import commands from main.py or make an event manager cog