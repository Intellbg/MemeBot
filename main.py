import discord
import os
from dic import index  # Import Meme Dictionary
client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Bot Responses on send chat
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Text Responses 
    if message.content.startswith('papiivan'):
        await message.channel.send('Vale verga')

    if message.content.lower()=="jaime":
        await message.channel.send(file=discord.File('img/ylasnenas.jpg'))
    
    if message.content.lower()=='memeindex':
        response=''
        for i in index.keys():
            response=i+"\n"+response
        await message.channel.send(response)

    #Meme Image Response key term #
    if message.content.startswith('#'):
        await message.channel.send(file=discord.File(index[message.content[1:].lower()]))
    #text -> TeXt
    if message.content.startswith('/rt'):
        holder=message.content
        await message.delete()          
        await holder.edit(content=tExTiNg(message.content[4:]))

def tExTiNg(message):
    index=0
    message=message.lower()
    capitalizeChar=True
    endMessage=""
    for char in message:
        if capitalizeChar:
            message[index]=message[index].upper()
        else: 
            message[index]=message[index]
        if char!=" ": 
            capitalizeChar=not(capitalizeChar)
        index+=1
    return endMessage
       


#Opens bot key and starts the bot
file=open("key.env",'r')
for i in file:
    client.run(i)
