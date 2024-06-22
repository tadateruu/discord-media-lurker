import discord
from discord.ext import commands, tasks
import os
import datetime

# ids to ignore logging
ignore_ids = {}

# initialize dirs
os.makedirs('media_logs', exist_ok=True)

client = commands.Bot(command_prefix="disvid ", intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="your shitposts"))
    print('Lurker is online :D')

@client.event
async def on_message(message):
    currenttime=datetime.datetime.now()
    # ignore bot and admins
    if message.author.bot:
        return
    if message.author.id in ignore_ids:
        return
    if message.attachments:
        for attachment in message.attachments:
            formatdt = currenttime.strftime("%Y-%m-%d_%H-%M-%S").replace(':', '_').replace('.', '_')
            await attachment.save(f'media_logs/{message.author.id}_{formatdt}_{attachment.filename}')
            print(f'Saved:{attachment.filename} from ID:{message.author.id}')

client.run('')
