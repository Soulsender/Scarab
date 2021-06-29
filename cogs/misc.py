from discord.ext import commands
import requests

class Misc(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Misc Online')
    
  @commands.command()
  async def insult(self, ctx):
    def get_insult():
      response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
      json_data = response.json()
      say_insult = json_data["insult"]
      return say_insult
    await ctx.send(get_insult())

  @commands.command()
  async def sheesh(self, ctx):
    # my friend asked me if I could add this
    await ctx.send("sheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesh")
    
def setup(client):
  client.add_cog(Misc(client))
