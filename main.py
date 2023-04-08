
# url : https://discord.com/api/oauth2/authorize?client_id=848987248711041094&permissions=8&scope=bot%20applications.commands
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
import requests
import random
import asyncio


load_dotenv()
token = os.getenv('TOKEN')
serverId = os.getenv('SERVERID')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await load()
    print("Bot is online")
    await bot.start(token)

asyncio.run(main())

# Default command prototype :

# @bot.command(aliases=[])
# async def ping(ctx):
#     await ctx.send("Pong")
