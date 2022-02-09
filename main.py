import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
bot = discord.Bot(auto_sync_commands=True, activity=discord.Game(name="now with slash commands!"))
# auto_sync_commands is a total piece of shit - always have this enabled

# load cogs
#bot.load_extension('cogs.dice_roll')
bot.load_extension('cogs.insults')
#bot.load_extension('cogs.into_server')
#bot.load_extension('cogs.mc_server')

@bot.slash_command(name='sourcecode', description='you can view the source code for my bot :)')
async def sourcecode(ctx):
  embed = discord.Embed(title="__Source Code__", color=0x4287f5)
  embed.add_field(name="Source code available on github", value="https://github.com/Soulsender/scarabbot", inline=False)
  await ctx.respond(embed=embed)

@bot.event
async def on_ready():
  print('{0.user} standing by'.format(bot))
  # DO NOT DO **ANYTHING** IN on_ready!

#keep_alive()
bot.run(os.environ['TOKEN'])