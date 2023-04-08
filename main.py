# bot token : ODQ4OTg3MjQ4NzExMDQxMDk0.G74RkY.sxUH3NpCrHyfmcz2xR0puH6XEnHhhmO6-d3WNE
# url : https://discord.com/api/oauth2/authorize?client_id=848987248711041094&permissions=8&scope=bot%20applications.commands
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot is online')


bot.run("ODQ4OTg3MjQ4NzExMDQxMDk0.G74RkY.sxUH3NpCrHyfmcz2xR0puH6XEnHhhmO6-d3WNE")