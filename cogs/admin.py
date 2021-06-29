from discord.ext import commands
import discord

class Admin(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Admin Online')

  '''@commands.command()
  async def createbotadmin(self, ctx):
    guild = ctx.guild
    await guild.create_role(name="Bot Admin")
    await ctx.send('Created @Bot Admin. Please be cautious, as any users you assign this role will be given admin permissions.')'''
  
  @commands.command()
  @commands.has_role("Bot Admin")
  async def purge(self, ctx, amount=5):
    await ctx.channel.purge(limit=amount)

  @commands.command()
  @commands.has_role("Bot Admin")
  async def kick(self, ctx, member : discord.Member):
    await member.kick()

  @commands.command()
  @commands.has_role("Bot Admin")
  async def ban(self, ctx, member : discord.Member):
    await member.ban()
    await ctx.send('Banned {member.metion}')

  @commands.command()
  @commands.has_role("Bot Admin")
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send('Unbanned {user.name}#{user.discriminator')
        return

def setup(client):
  client.add_cog(Admin(client))
