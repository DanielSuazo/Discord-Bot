from os import getenv
from time import sleep
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from random import randint
from csv import reader
from spotipy.oauth2 import SpotifyClientCredentials
import discord
import spotipy

# Load secret from .env file
load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

# Initialize bot
bot = commands.Bot(command_prefix = '.')
ID = 689640650768908309

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

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

@bot.command(name='eduardo', aliases = ["e", "edu"], brief = "A glimpse into the psyche of the genius known as Eduardo", help = "Responds with a quote from Eduardo")
async def eduardo(ctx):
  with open('quotes.csv', newline='') as csvfile:
    csv_quotes = reader(csvfile, delimiter=' ', quotechar='|')
    quotes = list(csv_quotes)
    x = randint(0, len(quotes)-1)
    msg = ""
    for i in quotes[x]:
      msg = msg + i + " "
    await ctx.send(f'{msg}')

@bot.command(name="bop")
async def bop(ctx):
  song_count = len(spotify.playlist_tracks("0uhzIssXs8d2tFGi3vNHCW")["items"])
  x = randint(0, song_count - 1)
  link = spotify.playlist_tracks("6qZnImkqxbRtL9FiwqHkGK")["items"][x]["track"]["external_urls"]["spotify"]
  await ctx.send(link)
bot.run(TOKEN)

#help