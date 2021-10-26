import discord, random, asyncio, os
from discord.ext import tasks
from dotenv import load_dotenv
import postgetter

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv("CHANNEL_ID")

client = discord.Client()

@tasks.loop(minutes=90.0)
async def auto_send():
    channel = await client.fetch_channel(CHANNEL_ID)
    pg = postgetter.PostGetter()
    await channel.send(pg.fetchNewPosts())

@client.event
async def on_ready():
    auto_send.start()

client.run(TOKEN)