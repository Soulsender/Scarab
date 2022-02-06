import discord
from discord.ext import commands
import requests
import os

class mc_server(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('server Online')
    
  @commands.slash_command(name='server', description='gives infomation about the minecraft server')
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
    await ctx.respond(embed=embed)

def setup(client):
  client.add_cog(mc_server(client))