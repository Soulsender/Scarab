import requests
from discord.ext import commands

class reddit(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print(__file__)

  subreddit = "masterhacker"
  listing = "top"
  timeframe = "day"
  
  f"https://www.reddit.com/r/{subreddit}/{listing}.json?limit=1&t={timeframe}"


def setup(client):
  client.add_cog(reddit(client))