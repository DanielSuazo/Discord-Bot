from os import getenv
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import discord
# import youtube_dl

# Load secret from .env file
load_dotenv()
token = getenv("DISCORD_TOKEN")

# Initialize bot
bot = commands.Bot(command_prefix = '.')
ID = 420220660493844482 # 689640650768908309 #id of "Secret Werewolf" server


@bot.event
async def on_ready():
  print(f"{bot.user.name} has connected to Discord! (id: {bot.user.id})")
  for i in bot.guilds:
    print(i.name, i.id)

@bot.command()
async def killme(ctx):
  print("did it work?")
  await ctx.send("how may i help you?")

@bot.event
async def on_message(message):
  id = bot.get_guild(ID)

  if message.content.find("!hello") != -1:
    await message.channel.send("Hi") 
  elif message.content == "!users":
    await message.channel.send(f"# of Members: {id.member_count}") 


bot.run(token)