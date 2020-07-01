from os import getenv
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from random import randint
from csv import reader
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
  await ctx.send("how may i help you?")

@bot.command()
async def why(ctx):
  await ctx.send("why hello there")

@bot.command()
async def eduardo(ctx):
  with open('quotes.csv', newline='') as csvfile:
    csv_quotes = reader(csvfile, delimiter=' ', quotechar='|')
    quotes = list(csv_quotes)
    x = randint(0, len(quotes)-1)
    msg = ""
    for i in quotes[x]:
      msg = msg + i + " "
    await ctx.send(f'{msg}')

bot.run(TOKEN)

#help