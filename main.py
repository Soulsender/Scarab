import discord
import os
import requests
import random
import json
from keep_alive import keep_alive


client = discord.Client()
bot_token = os.environ['TOKEN']

# create def commands

def get_insult():
  response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
  json_data = response.json()
  say_insult = json_data["insult"]
  return say_insult

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

@client.event
async def on_ready():
  print('{0.user} standing by'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='$help'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='In Maintenance'))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('$insult'):
      await message.channel.send(get_insult())

    if message.content.startswith('$server'):
      players_online = get_serverplayers()
      is_online = get_serverinfo()
      if is_online:
        onlineview = ':white_check_mark: - Server is up and running'   
      if not is_online:
        onlineview = ':x: - Server is down '

      embedVar = discord.Embed(title="__Server Info__", description="Collection of infomation regarding server IP, status, and changes. \n Please keep in mind data *ONLY* updates every 5 minutes or so.", color=0x00ff00)
      embedVar.add_field(name="Connection Info", value="IP - 142.44.145.32 \n PORT - 25626",inline=False)
      embedVar.add_field(name="Current Status", value=onlineview, inline=False)
      embedVar.add_field(name="Players Online", value=players_online + '/20', inline=False)
      await message.channel.send(embed=embedVar)   
      

    # create basic replies

    if message.content =='$help':
      embedVar = discord.Embed(title="__Command Menu__", color=0x2b2a2a)
      embedVar.add_field(name="Useful", value="$help - send help menu \n $server - get infomation about our minecraft server \n $market - open the market (WIP) \n $roll - open dice roll menu",inline=False)
      embedVar.add_field(name="Miscellanous", value='$insult - send randomly generated insult \n $hello - say hello! \n $sheesh - sheesh \n $wap - no please dont', inline=False)
      await message.channel.send(embed=embedVar)

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

    if message.content == '$roll':
      embedVar = discord.Embed(title="__Dice Roll Menu__", color=0x4287f5)
      embedVar.add_field(name="Dice Types", value="D20 \n D12 \n D10 \n D100 \n D8 \n D6 \n D4 \n\n Use command with **$roll {dice}**",inline=False)
      await message.channel.send(embed=embedVar)

    if message.content == '$hello':
      await message.channel.send("Hello!")

    if message.content == '$wap':
      f = open("wop.txt", 'r')
      for word in f:
        await message.channel.send(word)

    if message.content == 'cringe':
      await message.channel.send("^ haha idiot")

    if message.content == 'pog':
      await message.channel.send("https://tenor.com/view/lizard-dancing-poggers-lizard-dance-poggers-gif-18527737")
      
    if message.content == '$sheesh':
      await message.channel.send("sheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesh")   

keep_alive()
client.run(os.getenv('TOKEN'))