import discord
import os
client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('papiivan'):
        await message.channel.send('Vale verga')

    if message.content.startswith("jaime"):
        await message.channel.send('Y las nenas ?')
      
    if message.content.startswith('vecerdomiserable'):
        await message.channel.send(file=discord.File('img/vecerdomiserable.jpg'))


client.run(os.getenv('TOKEN'))
