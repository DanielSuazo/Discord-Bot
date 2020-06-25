# bot.py
import os
import time
from discord.ext import commands
from dotenv import load_dotenv
import discord

ffmpeg_options = {
    'options': '-vn'
}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = 420220660493844482

bot = commands.Bot(command_prefix = '>')

@bot.event
async def on_ready():
    print(discord.utils.get(bot.guilds, name=GUILD))
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user.id} is connected to the following guild:\n'
        
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    
@bot.command(name='monkagun', aliases = ["mg"], brief = 'Removes specified user from whatever voice channel they are currently connected too.', help = 'Removes user from channel while also posting a photo of Monkagun, requires argument [user] to be username, not a nickname.')
#@commands.has_permissions(administrator = True)
async def monkagun(ctx, user: discord.Member = None):
    if (user == None):
        await ctx.send("```css\nError: Missing Argument, no user specified.```")
    if (user.voice == None):
        await ctx.send("```css\nError: User is not in any Voice Channel.```")
    else:
        voice = await user.voice.channel.connect()  
        audio = discord.FFmpegPCMAudio('audio.mp3')
        ctx.voice_client.play(audio, after=None)
        time.sleep(1.5)
        await ctx.send("Out with you", file = discord.File('guan.jpg'))
        await user.move_to(None)
        await ctx.voice_client.disconnect()

@bot.command(name='kitchengun', aliases = ["kg"], brief = 'Plays Kitchen Gun.', help = 'Joins Authors Voice Channel and plays "I love You Kitchen Gun')
async def kitchengun(ctx):
    await Play_Sound(ctx, "kitchengun.mp3", 2.0)
    
@bot.command(name='heyheyhey', aliases = ["hhh"], brief = 'Plays Hey Hey Hey', help = 'Joins Authors Voice Channel and plays "Hey hey Hey')
async def heyheyhey(ctx):
    await Play_Sound(ctx, "heyheyhey.mp3", 5.0)
    
@bot.command(name='bitconnect', aliases = ["bc"], brief = 'Plays BitConnect', help = 'Joins Authors Voice Channel and plays "BitConnect')
async def bitconnect(ctx):
    await Play_Sound(ctx, "bitconnect.mp3", 7.0)

@monkagun.error
async def monkagun_error(ctx, error):
    if isinstance(error, discord.ext.commands.BadArgument):
        await ctx.send("```css\nError: Could not find specified user.```")
        
@bot.command(name='intro', help = 'Monka Bot says Hi')
async def intro(ctx):
    response = "*Sweats*"
    await ctx.send(response)

@bot.command(name='kick', help = 'kick test')
@commands.has_permissions(administrator = True)
async def kick(ctx, username):
    await ctx.send("kicking " + username)
    
@bot.command(name='join', help = 'join test')
async def join(ctx, voice_channel: commands.VoiceChannelConverter):
    try:
        await voice_channel.connect()
    except commands.BotMissingPermissions as error:
        await ctx.send("Unable to join Voice Channel.")
    await ctx.send(f"I have joined: {voice_channel}")
    
@bot.command(name='deletethis', aliases = ["dt"], brief = 'Delete This', help = "Delete This")
async def deletethis(ctx):
        await ctx.send("Delete dis.", file = discord.File('picture_assets/monkagun.png'))
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct permission for this command.')
    
#General User Repetitive Functions
async def Play_Sound(ctx, sound: str, delay: float):

    if (ctx.author.voice == None):
        await ctx.send("```css\nError: You are not in any Voice Channel.```")
    else:
        #sound = "sound_clips/" + sound
        voice = await ctx.message.author.voice.channel.connect()  
        audio = discord.FFmpegPCMAudio(sound)
        ctx.voice_client.play(audio, after=None)
        time.sleep(delay)
        await ctx.voice_client.disconnect()

bot.run(TOKEN)
