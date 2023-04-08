
# url : https://discord.com/api/oauth2/authorize?client_id=848987248711041094&permissions=8&scope=bot%20applications.commands
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Bot is online')


bot.run(token)
