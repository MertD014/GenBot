#https://twentysix26.github.io/Red-Docs/red_commands/ 
#https://replit.com/@aeri/aebrie
#useful link to get ideas for new commmands and modules
#modular programming go brrrrrrr

import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import cogs.voice as voice
import cogs.moderation as moderation
import cogs.general as general
from keepAlive import keep_alive

keep_alive()                                    #works fine for now but need rework

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
botPrefix = "."
bot = commands.Bot(command_prefix=botPrefix, intents = intents)                       #ability to change botPrefix

@bot.event
async def on_ready():
  async for guild in bot.fetch_guilds(limit=100):
    print(f"Connected to {guild.name}")                                                             #print total no guilds and users
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
  if after.status is discord.Status.streaming:
    await after.guild.system_channel.send(f"@everyone {after.mention} is streaming! Go check it out") #get stream info


    --->whitelist
"""

@bot.command()
async def s2s(ctx):
  await ctx.send("ZİH̨̢̀İ͚̹Ņ͟͝SE͎͔̪L̖ ̅̏̃҉SO̅RU̿͂ͣǸ̅̏ ͋̅͊Y̷̸͟Aͯ̋̈RDIͫ̄͠M̄̃̏ ͑ͪͬE̒̎ͫDİͥ̌͑N\nMENTAL COKUNTU\n⣿⣯⣿⣿⣿⣶⣶⣶⣶⣤⣤⣤⣀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷\n　　⠈⠻⣿⡛⠉⠭⠉⠉⢉⣿⣿⣧\n⠲⣶⠖⠄⠄⢿⣿⠄⠶⣶⣾⣿⣿⣿⣿⣧\n　　　⠺⢿⡗⠄⣹⣿⣿⠿⣟⣿⡏\n　　　　⠤⠤⢾⣿⣿⣿⣦⠘⡿\n　　⠈⢻⡿⣷⣶⣶⣤⣤⣤⣶⣦\n　　　⣽⣿⣿⣿⣿⣿⣿⣿⣿⡟\n　　　⠘⠿⣿⣿⣿⣿⣿⣿⣿\n　　　　　⠉⠉⠛⠋\nAkıl sağlığını\nĀ̴ ̈́̋͌ ͋̀͌ ̡̥͔t̵̛̔ ͛̾̉ ̀͐͝ ͕͈͖ì̶͠ ̑̉̃l̵̇̔l̶̇͠ ̽͗̓kaybet\n̯̬ ̸̲̀K̷̅̾ ̧̜͙.̷̓̕ ͊̐͒ ̛̀͊ ̶̆̅ ̭̞̦ ̲̞̙İ̴͆͝ ̹̥̩z̷̀̈l̶̇͠e̵̅͑ ̸ ̀͘͠ ̅̋̏l̵͘͘ ̾̉̏ ̋̏͌ ̝͖̭a̸̔ yk")


#Here we go!

bot.add_cog(general.General(bot))
bot.add_cog(moderation.Moderation(bot))
bot.add_cog(voice.Music(bot))

bot.run(DISCORD_TOKEN)