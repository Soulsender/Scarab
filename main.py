import discord
import os
from keep_alive import keep_alive
from discord.ext.commands import Bot
from discord.ext import commands


client = commands.Bot(command_prefix="$")
client.remove_command('help')


@client.command()
async def load(ctx, extension):
  client.load_extension('cogs.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension('cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
  print('{0.user} standing by'.format(client))

  # DO NOT DO ANYTHING IN on_ready!
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='$help'))
  #await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name='In Maintenance'))

@client.event
async def on_guild_join(guild: discord.Guild) -> None:
  if guild.system_channel == None:
    print('There is no system channel')
    if guild.rules_channel == None:
      print('There is no rule channel')




    else:
      print(guild.rules_channel, 'is the rules channel')
  else:
    print(guild.system_channel, 'is the system channel')


















  '''embed = discord.Embed(title="Hello!", color=0xeb4034)
  embed.add_field(name="My name is Scarab!", value="I am a multipurpose bot! You can see many of my functions using the $help command. \n\n On joining this server, I have created a role named @Bot Admin. Please give this role to anyone you grant admin permissions.",inline=False)
  channel = guild.get_channel(id)
  channel.send(embed=embed)
  await guild.create_role(name="Bot Admin")'''

@client.command()
async def adminhelp(ctx):
  embed = discord.Embed(title="__Admin Menu__", color=0xeb4034)
  embed.add_field(name="Commands", value="\n $ban {user} - bans user \n $kick {user} - kicks user \n $unban {user} - unbans user \n $purge {number of messages} - deletes set number of messages in current channel \n $createbotadmin - creates @Bot Admin role \n\n **BE ADVISED:** ANYONE WITH ROLE @Bot Admin WILL BE GIVEN THESE PERMISSIONS. \n *If this role does not exist, please make one using $createbotadmin (NOTE: This is disabled at the moment).*",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def sourcehelp(ctx):
  embed = discord.Embed(title="__Source Code__", color=0x4287f5)
  embed.add_field(name="Source code available on github", value="https://github.com/Soulsender/scarabbot",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  embed = discord.Embed(title="__Command Menu__", color=0x2b2a2a)
  embed.add_field(name="Useful", value="$server - get infomation about our minecraft server \n $market - open the market (WIP) \n $rollhelp - open dice roll menu",inline=False)
  embed.add_field(name="Miscellanous", value='$insult - send randomly generated insult \n $sheesh - sheesh', inline=False)
  embed.add_field(name="Menus", value='$rollhelp - dice roll menu \n $adminhelp - admin menu \n $sourcehelp - view the bot source code \n $help - send help menu', inline=False)
  await ctx.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))
