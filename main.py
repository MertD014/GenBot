import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import cogs.voice as voice
import cogs.moderation as moderation
import cogs.general as general
from keepAlive import keep_alive

keep_alive()

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
botPrefix = "."
bot = commands.Bot(command_prefix=botPrefix, intents = intents)

@bot.event
async def on_ready():
  async for guild in bot.fetch_guilds(limit=100):
    print(f"Connected to {guild.name}")
  print("Ready to go!")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Missing arguments!')
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have permission to use that command!")

#Here we go!

bot.add_cog(general.General(bot))
bot.add_cog(moderation.Moderation(bot))
bot.add_cog(voice.Music(bot))

bot.run(DISCORD_TOKEN)