#https://twentysix26.github.io/Red-Docs/red_commands/ 
#https://replit.com/@aeri/aebrie
#useful link to get ideas for new commmands and modules
#modular programming go brrrrrrr

import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from keepAlive import keep_alive

import cogs.voice as voice
import cogs.moderation as moderation
import cogs.general as general
#import cogs.xp as xp




keep_alive()                                    #works fine for now but need rework

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
botPrefix = "."
bot = commands.Bot(command_prefix=botPrefix, intents = intents)                       #ability to change botPrefix

@bot.event
async def on_ready():
  async for guild in bot.fetch_guilds(limit=100):
    print(f"Connected to {guild.name}")                                                 #print total no guilds and users
  await bot.change_presence(status=discord.Status.online, activity=discord.Game("with the API"))    #add more variations
  print("Ready to go!")

@bot.event
async def on_guild_join(guild):                                                             #embed and send a single message
    if guild.system_channel is not None: 
        await guild.system_channel.send(f'Thanks for inviting me to {guild.name}')
        await guild.system_channel.send(f'For more info type .help ^^')

@bot.event
async def on_member_join(member):           #add more variation to message
    guild = member.guild                                                      
    await guild.system_channel.send(f"Welcome to {guild.name} {member.mention}!")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Missing arguments!')
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have permission to use that command!")

"""
@bot.event
async def on_member_update(before, after):
  if before.activity.type is not discord.ActivityType.streaming and after.activity.type is discord.ActivityType.streaming:
    await after.guild.system_channel.send(f"{after.mention} is streaming on {after.activity.platform}: {after.activity.name}.\nJoin here: {after.activity.url}")
"""



#Here we go!

bot.add_cog(general.General(bot))
bot.add_cog(moderation.Moderation(bot))
bot.add_cog(voice.Music(bot))
#bot.add_cog(xp.Xp(bot))                       why broken bruh

bot.run(DISCORD_TOKEN)