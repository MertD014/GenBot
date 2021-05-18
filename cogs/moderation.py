import discord
from discord.ext import commands
import asyncio

defaultBanReason = "no reason"
defaultKickReason = "no reason"
defaultWarnReason = "no reason"

class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(brief='Ban members to punish them.', description='Ban users with their tags!')
  @commands.has_permissions(ban_members = True)
  async def ban(self, ctx, member : discord.Member = None, *, reason=None):
    if member is None:
      return await ctx.send("Please mention someone to ban!")
    if reason is None:
      reason = defaultBanReason
    await ctx.send(f'Banned {member.mention} for {reason}.')
    await ctx.guild.ban(member, reason=reason)

  @commands.command(brief='Unban old member for a second chance!', description='To unban use name#---- (tags does not work)')
  @commands.has_permissions(administrator = True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
      user = ban_entry.user
      if(user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}.')
        return
    await ctx.send("No match! Please check your input!")


  @commands.command(brief='Kick members if you need to :)', description='Kick members with their tags.')
  @commands.has_permissions(kick_members = True)
  async def kick(self, ctx, member : discord.Member = None, *, reason=None):
    if member is None:
      return await ctx.send("Please mention someone to kick!")
    if reason is None:
      reason = defaultKickReason
    await ctx.send(f'Kicked {member.mention} for {reason}.')
    await ctx.guild.kick(member, reason=reason)

  @commands.command(brief='Warn members before punishing.', description='Warn members with their tags')
  @commands.has_permissions(kick_members = True)
  async def warn(self, ctx, member : discord.Member = None, *, reason=None):
    if member is None:
      return await ctx.send("Please mention someone to kick!")
    if reason is None:
      reason = defaultWarnReason
    await member.send(f"You have been warned for {reason} at {member.guild.name}. Be careful as more warnings can result in a ban!")

  @commands.command(pass_context = True)
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx):
    await ctx.message.channel.purge()


  @commands.command()
  @commands.has_guild_permissions(mute_members=True)
  async def mute(self, ctx, member : discord.Member = None, *, reason=None):
    await member.edit(mute = True)

  @commands.command()
  @commands.has_guild_permissions(mute_members=True)                       #guild permission r&d needed
  async def unmute(self, ctx, member : discord.Member = None):              #balckfury special easter egg dm
    await member.edit(mute = False)

  @commands.command()
  @commands.has_permissions(manage_nicknames=True)
  async def nick(self, ctx, member : discord.Member = None, *, newNick):
    await member.edit(nick = newNick)
