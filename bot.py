import os
import discord
import asyncio
global str

client = discord.Client()
szukane="stand"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.nick == 'Jotaro' or message.author.nick == 'Jokero':
        tmp = await client.send_message(message.channel, 'Woof!')

client.run(os.getenv('TOKEN'))
