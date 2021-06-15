import discord
from discord.ext import commands
import requests

class Useful(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def server(self, ctx):
    def get_serverinfo():
      response = requests.get("https://api.mcsrvstat.us/bedrock/2/142.44.145.32:25626")
      json_data = response.json()
      say_serverinfo = json_data["players"]['online']
      return say_serverinfo
    def get_serverplayers():
      response = requests.get("https://api.mcsrvstat.us/bedrock/2/142.44.145.32:25626")
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
    embed.add_field(name="Dice Types", value="D20 \n D12 \n D10 \n D100 \n D8 \n D6 \n D4 \n\n Use command with **$roll {dice}**",inline=False)
    await ctx.send(embed=embed)

  @commands.command()
  async def roll(ctx, dicetype=20, dicenum=1):
    return
  
'''
  if message.content == '$roll d20':
    value = random.randint(1, 20)
    await message.channel.send('**Rolled a D20!**')
    if value == 20:
      await message.channel.send('**NAT 20!**')
    else:
      await message.channel.send(value)

  if message.content == '$roll d12':
    value = random.randint(1, 12)
    await message.channel.send('**Rolled a D12!**')
    await message.channel.send(value)

  if message.content == '$roll d10':
    value = random.randint(1, 10)
    await message.channel.send('**Rolled a D10!**')
    await message.channel.send(value)

  if message.content == '$roll d100':
    value = random.randint(1, 100)
    await message.channel.send('**Rolled a D100!**')
    await message.channel.send(value)

  if message.content == '$roll d8':
    value = random.randint(1, 8)
    await message.channel.send('**Rolled a D8!**')
    await message.channel.send(value)

  if message.content == '$roll d6':
    value = random.randint(1, 6)
    await message.channel.send('**Rolled a D6!**')
    await message.channel.send(value)

  if message.content == '$roll d4':
    value = random.randint(1, 4)
    await message.channel.send('**Rolled a D4!**')
    await message.channel.send(value)

'''



def setup(client):
  client.add_cog(Useful(client))