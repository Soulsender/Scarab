import discord
import os
from discord.ext import commands

from colorama import Fore

intents = discord.Intents.default()
intents.members = True
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix="$", activity = discord.Game(name="$help"), intents=intents)
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
  # init sequence, only print statements allowed
  print("===== BOT INITILIZATION =====")
  print(Fore.GREEN, '{0.user} standing by'.format(client), Fore.RESET)
  print("===== SERVERS LOADED =====")
  print(Fore.BLUE, '\n'.join(guild.name for guild in client.guilds), Fore.RESET)
  print("===== MODULES LOADED =====", Fore.YELLOW)
  

# mimic
@client.command()
@commands.has_role('Bot Admin') # Checks for Administrator rank.
async def mimic(ctx, *, question):
  await ctx.message.delete()
  await ctx.send(f'{question}')
  print('{0.user} standing by'.format(client))
  # DO NOT DO ANYTHING IN on_ready!
 
@client.event
async def on_member_join(member):
  print("user joined")
  verify_channel = client.get_channel("channel_id")
  await verify_channel.send(f"@{member}, to verify, use the `/verify` command!")

@client.event
async def on_member_join(member):
  print("user joined")
  verify_channel = client.get_channel(821967030622093313)
  await verify_channel.send(f"@{member}, to verify, use the `/verify` command!")
  
@client.command()
async def sourcehelp(ctx):
  embed = discord.Embed(title="__Source Code__", color=0x4287f5)
  embed.add_field(name="Source code available on github", value="https://github.com/Soulsender/scarabbot",inline=False)
  await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  embed = discord.Embed(title="__Command Menu__", color=0x2b2a2a)
  embed.add_field(name="Useful", value="$rollhelp - open dice roll menu",inline=False)
  embed.add_field(name="Miscellanous", value='$insult - send randomly generated insult', inline=False)
  embed.add_field(name="Menus", value='$rollhelp - dice roll menu \n $sourcehelp - view the bot source code \n $help - send this help menu', inline=False)
  await ctx.send(embed=embed)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  # number is the user ID of the victim
  if message.author.id == 259947663821111306:
    await message.channel.send('🤓')
  # elif "arch" in message.content:
  #   await message.channel.send('🤓')
  #   await message.channel.send('i uSe ArCh bTW!!!1!11')
  # elif "ARCH" in message.content:
  #   await message.channel.send('🤓')
  #   await message.channel.send('i uSe ArCh bTW!!!1!11')
  # elif "Arch" in message.content:
  #   await message.channel.send('🤓')
  #   await message.channel.send('i uSe ArCh bTW!!!1!11')
  # elif "mart" in message.content:
  #   await message.channel.send('🤓')
  #   await message.channel.send('guys have i told you that wingdings is just a font?')

@client.command()
async def servers(ctx):
  servers = list(client.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")
  await ctx.send('\n'.join(guild.name for guild in client.guilds))
@commands.has_role('Bot Admin') # Checks for Administrator rank.
async def mimic(ctx, *, question):
  await ctx.message.delete()
  await ctx.send(f'{question}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  # number is the user ID of the victim
  if message.author.id == 259947663821111306:
    await message.channel.send('🤓')
  if "arch" in message.content:
    await message.channel.send('🤓')
    await message.channel.send('i uSe ArCh bTW!!!1!11')

client.run(str(os.getenv('TOKEN')))