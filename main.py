import discord
import os
client=discord.Client()
dic={
'otrafiestadehomosexuales':'img/otrafiestadehomosexuales.jpg',
'ytueresunpavo':'img/ytueresunpavo.jpg',
'terribleoremos':'img/terribleoremos.jpg',
'algoandamal':'img/algoandamal.jpg',
'serricoesmalo.':'img/serricoesmalo.jpeg',
'chicolisto':'img/chicolisto.jpg',
'lag':'img/lag.jpg',
'vistete':'img/vistete.jpg',
'kowalskianalisis':'img/kowalskianalisis.jpg',
'violentopana':'img/violentopana.jpg',
'decabeza':'img/decabeza.jpg',
'observe':'img/observe.jpg',
'bailarina':'img/bailarina.jpg',
'asiesmaster':'img/asiesmaster.jpg',
'waisousirius.':'img/waisousirius.jpeg',
'piposad':'img/piposad.jpg',
'pensarcorrectoesloquehago':'img/pensarcorrectoesloquehago.jpg',
'noseasegoista.':'img/noseasegoista.jpeg',
'ustedesestanenfermos':'img/ustedesestanenfermos.jpg',
'eresmaricon':'img/eresmaricon.jpg',
'terriblerobemos':'img/terriblerobemos.jpg',
'wecreeme':'img/wecreeme.jpg',
'quepiensasyubarta':'img/quepiensasyubarta.jpg',
'quedijisteestupido':'img/quedijisteestupido.jpg',
'yapuedoluchaar':'img/yapuedoluchaar.png',
'semamo':'img/semamo.jpg',
'cheems':'img/cheems.jpg',
'nomamesqueasco':'img/nomamesqueasco.jpg',
'expropiese':'img/expropiese.jpg',
'ahivaotro':'img/ahivaotro.jpg',
'amiajoketoyou':'img/amiajoketoyou.jpg',
'expropiese1':'img/expropiese1.jpg',
'losoñe':'img/losoñe.jpg',
'conspiracion':'img/conspiracion.jpg',
'vecerdomiserable':'img/vecerdomiserable.jpg',
'nuncaesperenada':'img/nuncaesperenada.jpg',
'ylasnenas':'img/ylasnenas.jpg',
'esbellisimo':'img/esbellisimo.jpg',
'tengomiedo':'img/tengomiedo.jpg',
'olabb':'img/olabb.jpg',
'thatsdeep':'img/thatsdeep.jpg',
'queeresmaricon':'img/queeresmaricon.jpg',
'stonks':'img/stonks.jpg',
'queagradablesujeto':'img/queagradablesujeto.jpg',
'acercandoseelpeligrovieneya':'img/acercandoseelpeligrovieneya.jpg',
'papapa':'img/papapa.png',
'terminastelosdeberes':'img/terminastelosdeberes.jpg',
'pikachu':'img/pikachu.jpg',
}
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

    if message.content.startswith('/'):
        await message.channel.send(file=discord.File(dic[message.content[1:]]))


client.run(os.getenv('TOKEN'))
