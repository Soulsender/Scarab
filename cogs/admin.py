from discord.ext import commands

class Admin(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  def guild_owner_only():
    async def predicate(ctx):
        return ctx.author == ctx.guild.owner  # checks if author is the owner
    return commands.check(predicate)
  
  @commands.Cog.listener()
  async def on_ready(self):
    print(__file__)
  
  # @commands.command()
  # async def adminhelp(self, ctx):
  #   embed = discord.Embed(title="__Admin Menu__", color=0xeb4034)
  #   embed.add_field(name="Commands", value="\n $ban {user} - bans user \n $kick {user} - kicks user \n $unban {user} - unbans user \n $purge {number of messages} - deletes set number of messages in current channel \n $createbotadmin - creates @Bot Admin role \n\n **BE ADVISED:** ANYONE WITH ROLE @Bot Admin WILL BE GIVEN THESE PERMISSIONS. \n *If this role does not exist, please make one using $createbotadmin (NOTE: This is disabled at the moment).*",inline=False)
  #   await ctx.send(embed=embed)

  # @commands.command()
  # @guild_owner_only()
  # async def createbotadmin(self, ctx):
  #   guild = ctx.guild
  #   await guild.create_role(name="Bot Admin")
  #   await ctx.send('Created @Bot Admin. Please be cautious, as any users you assign this role will be given admin permissions.')
  
  # @commands.command()
  # @commands.has_role("Bot Admin")
  # async def purge(self, ctx, amount=5):
  #   await ctx.channel.purge(limit=amount)

  # @commands.command()
  # @commands.has_role("Bot Admin")
  # async def kick(self, ctx, member : discord.Member):
  #   await member.kick()

  # @commands.command()
  # @commands.has_role("Bot Admin")
  # async def ban(self, ctx, member : discord.Member):
  #   await member.ban()
  #   await ctx.send('Banned {member.metion}')

  # @commands.command()
  # @commands.has_role("Bot Admin")
  # async def unban(self, ctx, *, member):
  #   banned_users = await ctx.guild.bans()
  #   member_name, member_discriminator = member.split('#')
  #   for ban_entry in banned_users:
  #     user = ban_entry.user
  #     if (user.name, user.discriminator) == (member_name, member_discriminator):
  #       await ctx.guild.unban(user)
  #       await ctx.send('Unbanned {user.name}#{user.discriminator')
  #       return

def setup(client):
  client.add_cog(Admin(client))
