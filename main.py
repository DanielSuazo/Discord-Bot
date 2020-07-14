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


@bot.command(name="bop", aliases = ["b"], brief = "Gives you more songs to listen to", help = "Responds with a random song from the front page of r/listentothis")
async def bop(ctx):
  song_count = len(spotify.playlist_tracks("0uhzIssXs8d2tFGi3vNHCW")["items"])
  x = randint(0, song_count - 1)
  link = spotify.playlist_tracks("6qZnImkqxbRtL9FiwqHkGK")["items"][x]["track"]["external_urls"]["spotify"]
  await ctx.send(link)


@bot.command(name="d20")
async def d20(ctx):
  x = randint(0, 1)
  switch = [fuck_you, ily]
  await switch[x](ctx)


async def fuck_you(ctx):
  await ctx.send("fuck you")

async def ily(ctx):
  await ctx.send("i love you")

bot.run(TOKEN)