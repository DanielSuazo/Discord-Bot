from os import getenv
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import discord

# Load secret from .env file
load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

# Initialize bot
bot = commands.Bot(command_prefix = '.')
ID = 689640650768908309

@bot.event
async def on_ready():
  print(f"{bot.user.name} has connected to Discord! (id: {bot.user.id})")
  for i in bot.guilds:
    print(i.name, i.id)

@bot.command()
async def killme(ctx):
  print("did it work?")
  await ctx.send("how may i help you?")

@bot.command()
async def why(ctx):
  await ctx.send("why hello there")

bot.run(TOKEN)