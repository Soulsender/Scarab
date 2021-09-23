import discord
from discord.ext import commands
import requests
import random
import os

class Useful(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Use Online')
    
  @commands.command()
  async def server(self, ctx):
    #https://api.mcsrvstat.us/2/172.105.27.82

    def get_serverinfo():
      string = ("https://api.mcsrvstat.us/2/" + os.getenv('SERVER'))
      response = requests.get(string)
      json_data = response.json()
      say_serverinfo = json_data['online']
      return say_serverinfo

    def get_serverplayers():
      string = ("https://api.mcsrvstat.us/2/" + os.getenv('SERVER'))
      response = requests.get(string)
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
    embed.add_field(name="Connection Info", value=os.getenv('server'),inline=False)
    embed.add_field(name="Current Status", value=str(onlineview), inline=False)
    embed.add_field(name="Players Online", value=str(players_online) + '/20', inline=False)
    await ctx.send(embed=embed)

  @commands.command()
  async def rollhelp(self, ctx):
    embed = discord.Embed(title="__Dice Roll Menu__", color=0x1b006e)
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