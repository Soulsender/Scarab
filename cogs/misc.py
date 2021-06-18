from discord.ext import commands
import requests

class Misc(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def insult(self, ctx):
    def get_insult():
      response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
      json_data = response.json()
      say_insult = json_data["insult"]
      return say_insult
    await ctx.send(get_insult())

'''

if message.content == '$hello':
    await message.channel.send("Hello!")

if message.content == 'cringe':
  await message.channel.send("^ haha idiot")

if message.content == 'pog':
  await message.channel.send("https://tenor.com/view/lizard-dancing-poggers-lizard-dance-poggers-gif-18527737")
  
if message.content == '$sheesh':
  await message.channel.send("sheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesh")

'''

def setup(client):
  client.add_cog(Misc(client))
