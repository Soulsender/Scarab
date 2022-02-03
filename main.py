import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
from discord.ext import commands

load_dotenv()

client = commands.Bot(command_prefix="$", activity = discord.Game(name="$help"))
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

@client.command()
async def sourcehelp(ctx):
  embed = discord.Embed(title="__Source Code__", color=0x4287f5)
  embed.add_field(name="Source code available on github", value="https://github.com/Soulsender/scarabbot",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  embed = discord.Embed(title="__Command Menu__", color=0x2b2a2a)
  embed.add_field(name="Useful", value="$server - get infomation about our minecraft server \n $market - open the market (WIP) \n $rollhelp - open dice roll menu",inline=False)
  embed.add_field(name="Miscellanous", value='$insult - send randomly generated insult', inline=False)
  embed.add_field(name="Menus", value='$rollhelp - dice roll menu \n $adminhelp - admin menu \n $sourcehelp - view the bot source code \n $help - send this help menu', inline=False)
  await ctx.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))
