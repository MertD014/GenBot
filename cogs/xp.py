import discord
from discord.ext import commands
from discord.ext import tasks
import json
import random
import operator

class Xp(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.xpdata = dict()
    with open("data/xp.json", "r") as file:
      self.xpdata = json.load(file)
    self.saveXp.start()

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def givexp(self, ctx, member : discord.Member = None,  newXp : int = 0):
    self.xpdata[str(member.id)] = self.xpdata.get(str(member.id),0) + newXp
    
  @commands.command()
  @commands.has_permissions(administrator = True)
  async def setxp(self, ctx, member : discord.Member = None, newXp : int = 0):
    self.xpdata[str(member.id)] = int(newXp)

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def list(self, ctx):
    await ctx.send(dict(sorted(self.xpdata.items(), key=operator.itemgetter(1),reverse=True)))

  @commands.command()                                 #add aliases --- leaderboard
  async def top(self, ctx , no : int = 10):    
    no=min(no,len(list(self.xpdata.keys())))
    tempdict= dict(sorted(self.xpdata.items(no), key=operator.itemgetter(1),reverse=True))
    keylist=list(tempdict.keys())
    await ctx.send(tempdict)


  @commands.Cog.listener()
  async def on_message(self, message):
    if not message.author.bot:
      self.xpdata[str(message.author.id)] = self.xpdata.get(str(message.author.id),0) + random.randint(1,4)
  
  @tasks.loop(seconds=10.0)
  async def saveXp(self):
    with open("data/xp.json", "w") as file:
      json.dump(self.xpdata, file, indent = 4)
    

#voice channel xp
#partition of xpdata with guilds
#leaderboard command (.top .list .leaderboard)
