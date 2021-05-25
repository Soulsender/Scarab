import discord
import os
import requests
import random
import json
from keep_alive import keep_alive

client = discord.Client()
bot_token = os.environ['TOKEN']


def get_insult():
  response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
  #print(response.status_code)
  json_data = response.json()
  say_insult = json_data["insult"]
  return say_insult

def get_serverinfo():
  response = requests.get("https://api.mcsrvstat.us/bedrock/2/142.44.145.32:25626")
  json_data = response.json()
  say_serverinfo = json_data["online"]
  return say_serverinfo

def get_serverplayers():
  response = requests.get("https://api.mcsrvstat.us/bedrock/2/142.44.145.32:25626")
  json_data = response.json()
  say_serverplayers = json_data["players"]  
  return say_serverplayers

@client.event
async def on_ready():
  print('{0.user} standing by'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='$help'))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('$insult'):
      await message.channel.send(get_insult())

    if message.content.startswith('$server'):

      await message.channel.send('**IP -** 142.44.145.32 \n **PORT -** 25626')

      is_online = get_serverinfo()
      if is_online:
        await message.channel.send('**Server Status: ** :white_check_mark:')
      if not is_online:
        await message.channel.send("**Server Status: **:x: ")

      #await message.channel.send(get_serverplayers())
      print('test')
  










    if message.content.startswith('$hello'):
      await message.channel.send("Hello!")

    if message.content.startswith('cringe'):
      await message.channel.send("^ haha idiot")

    if message.content.startswith('pog'):
      await message.channel.send("https://tenor.com/view/lizard-dancing-poggers-lizard-dance-poggers-gif-18527737")
      
    if message.content.startswith('$sheesh'):
      await message.channel.send("sheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesh")

    if message.content.startswith('$help'):
      await message.channel.send("""\
     
         **SCARAB**
    **By Soulsender**

     **Commands:**
     $help - send help info

     $insult - send randomly generated insult 
     $server - get server IP and status (WIP)

     $hello - say hello
     $sheesh - sheesh""")

keep_alive()
client.run(os.getenv('TOKEN'))