import discord
from discord.ext import commands

defaultBanReason = "no reason"
defaultKickReason = "no reason"
defaultWarnReason = "no reason"

class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(brief='Ban members to punish them.', description='Ban users with their tags!')
  @commands.has_permissions(ban_members = True)
  async def ban(self, ctx, *, member : discord.Member = None, reason=None):
    if member is None:
      return await ctx.send("Please mention someone to ban!")
    if reason is None:
      reason = defaultBanReason
    await ctx.send(f'Banned {member.mention}.')
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
  async def kick(self, ctx, *, member : discord.Member = None, reason=None):
    if member is None:
      return await ctx.send("Please mention someone to kick!")
    if reason is None:
      reason = defaultKickReason
    await ctx.send(f'Kicked {member.mention}.')
    await ctx.guild.kick(member, reason=reason)

  @commands.command(brief='Warn members before punishing.', description='Warn members with their tags')
  @commands.has_permissions(kick_members = True)
  async def warn(self, ctx, *, member : discord.Member = None, reason=None):
    if member is None:
      return await ctx.send("Please mention someone to kick!")
    if reason is None:
      reason = defaultWarnReason
    await ctx.send(f'Kicked {member.mention}.')                  #kick user at warn threshold 