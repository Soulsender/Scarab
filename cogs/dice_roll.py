import discord
from discord.ext import commands
import random

class dice_roll(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print(__file__)

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
  client.add_cog(dice_roll(client))