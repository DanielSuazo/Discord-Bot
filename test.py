@bot.event
async def on_voice_state_update(member, before, after):
  if member.id == 725137838865383465 or member.id == 234395307759108106:
    return
  if before.channel == None and after.channel != None:
    client = await after.channel.connect()


    client.play(discord.FFmpegPCMAudio("audio.mp3", args=""), after=lambda e: print("im done"))
    client.source = discord.PCMVolumeTransformer(client.source)
    client.source.volume = 0.07
    sleep(2)
    await client.disconnect()