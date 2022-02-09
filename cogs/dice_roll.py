from discord.ext import commands
import random


class dice_roll(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('dice_roll Online')

  @commands.slash_command(name='roll', description='roll a specified dice and dice amount')
  async def roll(self, ctx, dicetype=20, dicenum=1):

    if dicenum <= 20:
      for _ in range(dicenum):
        await ctx.respond(str(random.randint((1, dicetype))))
    if dicenum > 20:
      await ctx.respond('Invalid number of rolls')
    else:
      await ctx.respond('Please try again, and specify dice and number.')

def setup(client: commands.Bot):
  client.add_cog(dice_roll(client))