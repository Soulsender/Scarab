from discord.ext import commands

class Admin(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot Online')
    
  @commands.command()
  async def purge(self, ctx, amount=5):
    await ctx.channel.purge(limit=amount)

  '''@commands.command()
  async def kick(self, ctx, member : discord.Member):
    await member.kick()

  @commands.command()
  async def ban(self, ctx, member : discord.Member):
    await member.ban()
    await ctx.send('Banned {member.metion}')

  @commands.command()
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send('Unbanned {user.name}#{user.discriminator')
        return'''

def setup(client):
  client.add_cog(Admin(client))
#