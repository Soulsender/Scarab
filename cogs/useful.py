import discord
from discord.ext import commands
import requests
import random
import json



class Useful(commands.Cog):
  def __init__(self, client):
    self.client = client

  def info(self, ctx, client, message):
    with open('serversetup.json', 'r') as f:
      ip = json.load(f)
      port = json.load(f)
      platform = json.load(f)
    return ip, port, platform[str(message.guild.id)]

  @commands.Cog.listener()
  async def on_guild_join(guild):
    with open('serversetup.json', 'r') as f:
      ip = json.load(f)
      port = json.load(f)
      platform = json.load(f)
    ip[str(guild.id)] = 'No ip selecte'
    port[str(guild.id)] = 'No port selected'
    platform[str(guild.id)] = 'No platform selected'
    with open('serversetup.json', 'w') as f:
      json.dump(ip, f, indent=2)
      json.dump(port, f, indent=2)
      json.dump(platform, f, indent=2)

  @commands.Cog.listener()
  async def on_guild_remove(guild):
    with open('serversetup.json', 'r') as f:
      ip = json.load(f)
      port = json.load(f)
      platform = json.load(f)
    ip.pop[str(guild.id)]
    port.pop[str(guild.id)]
    platform.pop[str(guild.id)]
    with open('serversetup.json', 'w') as f:
      json.dump(ip, f, indent=2)
      json.dump(port, f, indent=2)
      json.dump(platform, f, indent=2)

  @commands.command()
  async def setup(self, ctx, platform, ip, port):
    with open('serversetup.json', 'r') as f:
      ip = json.load(f)
      port = json.load(f)
      platform = json.load(f)
    ip[str(ctx.guild.id)] = ip
    port[str(ctx.guild.id)] = port
    platform[str(ctx.guild.id)] = platform
    with open('serversetup.json', 'w') as f:
      json.dump(ip, f, indent=2)
      json.dump(port, f, indent=2)
      json.dump(platform, f, indent=2)
    return ip, port, platform

  @commands.command()
  async def server(self, ctx):
  

    def get_serverinfo():
      response = requests.get("https://api.mcsrvstat.us/bedrock/2/ + ip +: + port")
      json_data = response.json()
      say_serverinfo = json_data["players"]['online']
      return say_serverinfo
    def get_serverplayers():
      response = requests.get("https://api.mcsrvstat.us/bedrock/2/ + ip + : + port")
      json_data = response.json()
      say_serverplayers = json_data['players']['online']
      return say_serverplayers

    players_online = get_serverplayers()
    is_online = get_serverinfo()

    if is_online:
      onlineview = ':white_check_mark: - Server is up and running'   
    if not is_online:
      onlineview = ':x: - Server is down'

    embed = discord.Embed(title="__Server Info__", description="Collection of infomation regarding server IP, status, and changes. \n Please keep in mind data *ONLY* updates every 5 minutes or so.", color=0x00ff00)
    embed.add_field(name="Connection Info", value="IP - 142.44.145.32 \n PORT - 25626",inline=False)
    embed.add_field(name="Current Status", value=onlineview, inline=False)
    embed.add_field(name="Players Online", value=players_online + '/20', inline=False)
    await ctx.send(embed=embed)

  @commands.command()
  async def rollhelp(self, ctx):
    embed = discord.Embed(title="__Dice Roll Menu__", color=0x4287f5)
    embed.add_field(name="Dice Types", value="D20 \n D12 \n D10 \n D100 \n D8 \n D6 \n D4 \n\n Use command with **$roll {dice type}  {# of dice}** \n Ex. *$roll 20 3*",inline=False)
    await ctx.send(embed=embed)

  @commands.command()
  async def roll(self, ctx, dicetype=20, dicenum=1):
    if dicenum <= 20:
      for _ in range(dicenum):
        await ctx.send(random.randint(1, dicetype))
    if dicenum > 20:
      await ctx.send('Invalid number of rolls')
 
def setup(client):
  client.add_cog(Useful(client))
#