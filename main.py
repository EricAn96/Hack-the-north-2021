import discord
import info


client = discord.Client()
TOKEN="ODg4Nzc2Mjg1MjMxMzg2NjM0.YUXnaw.xXM9xuX2RF2mzoRm3XU-41iXcUU"

@client.event
async def on_ready():
    print('We have logged in a {0.user}'.format(client))
    return


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content).lower()
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    # first index is the command, second is the param
    formattedlist = user_message.split(' ', 1)

    # help command (displays list of all commands with brief description)
    if formattedlist[0] == '~help':
        pass

    # global covid stats
    if formattedlist[0] == '~covid-global':
        pass

    # covid stats (region specific)
    # command: ~covid param(country name)
    if formattedlist[0] == '~covid':
        stats = info.covid_country(formattedlist[1])
        
        for key, value in stats.items():
            await message.channel.send(key + ': ' + str(value))