import discord
import os
from dic import dic
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

    if message.content.lower()=="jaime":
        await message.channel.send(file=discord.File('img/ylasnenas.jpg'))

    if message.content.startswith('#'):
        await message.channel.send(file=discord.File(dic[message.content[1:].lower()]))

    if message.content.lower()=='memeindex':
        response=''
        for i in dic.keys():
            response=i+"\n"+response
        await message.channel.send(response)

file=open("xd.env",'r')
for i in file:
    client.run(i)
