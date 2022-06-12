from discord.ext import commands
import discord

class into_server(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Into_server Online')

  @commands.Cog.listener()
  async def on_guild_join(self, ctx, guild: discord.Guild) -> None:
    embed = discord.Embed(title="Hello!", color=0xeb4034)
    embed.add_field(name="My name is Scarab!", value="I am a multipurpose bot! You can see many of my functions using the $help command. \n\n On joining this server, I have created a role named @Bot Admin. Please give this role to anyone you grant admin permissions.",inline=False)
    await guild.create_role(name="Bot Admin")

    if guild.system_channel == None:
      print('There is no system channel')
      if guild.rules_channel == None:
        print('There is no rule channel. Sending welcome message to first channel listed.')
        await guild.text_channels[0].send(embed=embed)

      else:
        print(guild.rules_channel, 'is the rules channel')
        await guild.text_channels[0].send(embed=embed)
        return
    else:
      print(guild.system_channel, 'is the system channel')
      await guild.text_channels[0].send(embed=embed)
      return

def setup(client):
  client.add_cog(into_server(client))