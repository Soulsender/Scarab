import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
bot = discord.Bot(auto_sync_commands=True, activity=discord.Game(name="now with slash commands!",))
# auto_sync_commands is a total piece of shit

@bot.command()
async def load(ctx, extension):
  bot.load_extension('cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension('cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def sourcehelp(ctx):
  embed = discord.Embed(title="__Source Code__", color=0x4287f5)
  embed.add_field(name="Source code available on github", value="https://github.com/Soulsender/scarabbot",inline=False)
  await ctx.respond(embed=embed)

@bot.event
async def on_ready():
  print('{0.user} standing by'.format(bot))
  # DO NOT DO **ANYTHING** IN on_ready!

@bot.slash_command(name="help", description="Commands and infomation")
async def help(ctx):
  embed = discord.Embed(title="__Command Menu__", color=0x2b2a2a)
  embed.add_field(name="Useful", value="$server - get infomation about our minecraft server \n $market - open the market (WIP) \n $rollhelp - open dice roll menu",inline=False)
  embed.add_field(name="Miscellanous", value='$insult - send randomly generated insult', inline=False)
  embed.add_field(name="Menus", value='$rollhelp - dice roll menu \n $adminhelp - admin menu \n $sourcehelp - view the bot source code \n $help - send this help menu', inline=False)
  await ctx.respond(embed=embed)

keep_alive()
bot.run(os.environ['TOKEN'])



