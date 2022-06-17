import requests
from discord.ext import commands

class reddit(commands.Cog):
  def __init__(self, client):
    self.client = client

  subreddit = "masterhacker"
  listing = "top"
  timeframe = "day"
  
  f"https://www.reddit.com/r/{subreddit}/{listing}.json?limit=1&t={timeframe}"


def setup(client):
  client.add_cog(reddit(client))