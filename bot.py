import os
import discord
import aiocron
from dotenv import load_dotenv
import postgetter

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@aiocron.crontab('*/5 * * * *')
async def getPosts():
    guild = discord.utils.get(client.guilds, name="madreloid's bots")
    channel = discord.utils.find(lambda x: x.name == "jobs-bot", guild.text_channels)
    if channel and channel.permissions_for(guild.me).send_messages:
        await channel.send(postgetter.PostGetter.fetchNewPosts())

client.run(TOKEN)