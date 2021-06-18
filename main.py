import discord
import os
from keep_alive import keep_alive
from discord.ext.commands import Bot
import json




client = Bot('$')
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
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='$help'))
  #await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name='In Maintenance'))

@client.command()
async def adminhelp(ctx):
  embed = discord.Embed(title="__Admin Menu__", color=0xeb4034)
  embed.add_field(name="Commands", value="\n $ban {user} - bans user \n $kick {user} - kicks user \n $unban {user} - unbans user \n $purge {number of messages} - deletes set number of messages in current channel",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  embed = discord.Embed(title="__Command Menu__", color=0x2b2a2a)
  embed.add_field(name="Useful", value="$server - get infomation about our minecraft server \n $market - open the market (WIP) \n $rollhelp - open dice roll menu",inline=False)
  embed.add_field(name="Miscellanous", value='$insult - send randomly generated insult \n $sheesh - sheesh', inline=False)
  embed.add_field(name="Menus", value='$rollhelp - dice roll menu \n $adminhelp - admin menu \n $help - send help menu', inline=False)
  await ctx.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))
#