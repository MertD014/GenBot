"""
thinking like maybe from reddit i can get the latest post of r/memes?
later a can merge this cog with the reddit one
"""

import discord
from discord.ext import commands
import asyncpraw
import os
import random
from dotenv import load_dotenv


load_dotenv()
REDDIT_ID = os.getenv("REDDIT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")

class Memes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.reddit = asyncpraw.Reddit(client_id=REDDIT_ID,client_secret=REDDIT_SECRET,user_agent='GenbotmemesfromR')
  
  @commands.command()
  async def meme(self,ctx):
    subreddit = await self.reddit.subreddit("memes")
    submission = await subreddit.random()
    await ctx.send(submission.url)




"""
submission = reddit.subreddit("memes").random()
    await ctx.send(submission.url)

maybe better??



@commands.command()
  async def meme(self,ctx):
    subreddit = await self.reddit.subreddit("memes")
    choice=random.randint(1,10)
    x=0
    async for submission in subreddit.hot(limit=10):
      x+=1
      if x==choice:
        await ctx.send(submission.url)

"""