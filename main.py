#https://twentysix26.github.io/Red-Docs/red_commands/ 
#https://replit.com/@aeri/aebrie
#useful link to get ideas for new commmands and modules
#modular programming go brrrrrrr

import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import json

import cogs.voice as voice
import cogs.moderation as moderation
import cogs.general as general
import cogs.xp as xp
import cogs.music as music





load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
defaultPrefix='.'


def get_prefix(client, message):
  with open('data/prefixes.json', 'r') as f:
    prefixes = json.load(f)
  return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=(get_prefix), intents = intents)




@bot.event
async def on_ready():
  noGuilds=0
  noUsers=0
  async for guild in bot.fetch_guilds(limit=100):
    noGuilds+=1
    #noUsers+=len(guild.members)
    print(f"Connected to {guild.name}")
  await bot.change_presence(status=discord.Status.online, activity=discord.Game("with the API"))    #add more variations
  print(f"With a total of {noUsers} users in {noGuilds} servers...")
  print(f"Ready to go!")

@bot.event
async def on_guild_join(guild):                                                     
  if guild.system_channel is not None: #embed and send a single message
    await guild.system_channel.send(f'Thanks for inviting me to {guild.name}')
    await guild.system_channel.send(f'For more info type .help ^^')
    
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
    prefixes[str(guild.id)] = defaultPrefix
  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
    prefixes.pop(str(guild.id))
  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)


@bot.event
async def on_member_join(member):                                                                   #add more variation to message
    guild = member.guild                                                      
    await guild.system_channel.send(f"Welcome to {guild.name} {member.mention}!")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Missing arguments!')
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have permission to use that command!")

bot.add_cog(general.General(bot))
bot.add_cog(moderation.Moderation(bot))
#bot.add_cog(voice.Music(bot))    #my music cog
bot.add_cog(music.Music(bot))     #someone elses music cog
#bot.add_cog(xp.Xp(bot))          #xp disabled need rework

bot.run(DISCORD_TOKEN)