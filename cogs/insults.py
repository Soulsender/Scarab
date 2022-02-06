from discord.ext import commands
import requests

class insults(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('insults Online')

  @commands.slash_command(name='insult', description='generates a random insult')
  async def insult(self, ctx):
    def get_insult():
      response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
      json_data = response.json()
      say_insult = json_data["insult"]
      return say_insult
    await ctx.respond(get_insult())
    
def setup(client):
  client.add_cog(insults(client))
