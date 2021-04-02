client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('ENTER TEXT YOU WANT TO SEND')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('TOKEN HERE', bot=False)
