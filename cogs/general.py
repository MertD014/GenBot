#import commands from main.py or make an event manager cog

import discord
from discord.ext import commands
import json

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def setprefix(self, ctx, prefix):
    with open('data/prefixes.json', 'r') as f:
      prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('data/prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix changed to: {prefix}')
  
  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'Pong! {int(self.bot.latency*1000)}ms')

