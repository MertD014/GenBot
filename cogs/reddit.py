import discord
from discord.ext import commands
import asyncpraw
import os
import random
from dotenv import load_dotenv


load_dotenv()
REDDIT_ID = os.getenv("REDDIT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")

class Reddit(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.reddit = asyncpraw.Reddit(client_id=REDDIT_ID,client_secret=REDDIT_SECRET,user_agent='GenbotmemesfromR')
  
  @commands.command()
  async def meme(self,ctx):
    subreddit = await self.reddit.subreddit("memes")
    submission = await subreddit.random()
    await ctx.send(submission.url)


  #enable/disable by admin
  @commands.command()
  async def nsfw(self,ctx):
    subreddit = await self.reddit.subreddit("nsfw")
    submission = await subreddit.random()
    await ctx.send(submission.url)

  @commands.command()
  async def randompostfrom(self,ctx,subredditname=None):
    subreddit = await self.reddit.subreddit(subredditname)
    submission = await subreddit.random()
    await ctx.send(submission.url)