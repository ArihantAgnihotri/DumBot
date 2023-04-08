
# url : https://discord.com/api/oauth2/authorize?client_id=848987248711041094&permissions=8&scope=bot%20applications.commands
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random
load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Default command prototype :

# @bot.command(aliases=[])
# async def ping(ctx):
#     await ctx.send("Pong")


@bot.event
async def on_ready():
    print('Bot is online')

GREETINGS = ["hi", "hola", "hello", "hey", "helloo", "hellooo",
             "good day", "greetings", "greeting", "good to see you",
             "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin",
             "how is everything", "how is everything going", "how's everything going", "how is you", "how's you",
             "how are things", "how're things", "how is it going", "how's it going", "how's it goin'",
             "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been",
             "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good",
             "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww",
             "g'day", "howdy"]

insults = ["You’re the reason God created the middle finger.",
           "If your brain was dynamite, there wouldn't be enough to blow your hat off.",
           "Light travels faster than sound which is why you seemed bright until you spoke",
           "You have so many gaps in your teeth it looks like your tongue is in jail.",
           "Your secrets are always safe with me. I never even listen when you tell me them.",
           "I forgot the world revolves around you. My apologies, how silly of me.", "Your face makes onions cry.",
           "You look so pretty. Not at all gross, today.", "I'm not insulting you, I'm describing you.",
           "I'm not a nerd, I'm just smarter than you.",
           "You bring everyone so much joy…when you leave the room.",
           "I thought of you today. It reminded me to take out the trash.",
           "Don't worry about me. Worry about your eyebrows.", "You are like a cloud. When you disappear it's a "
                                                               "beautiful day.",
           "Child, I've forgotten more than you ever knew.", "You have miles to go before you reach mediocre.",
           "I was today years old when I realized I didn’t like you.", "Wish I had a flip phone so I could slam "
                                                                       "it shut on this conversation.",
           "I'm busy right now, can I ignore you another time?", "Beauty is only skin deep, but ugly goes clean "
                                                                 "to the bone"]

emojis_love = ['😍', '😘', '🥰', '😙', '😚', '☺', '😊', '🤭', '👄']
emojis_sad = ['😑', '😥', '😔', '😕', '☹', '🙁',
              '😖', '😞', '😟', '😢', '😭', '😧', '😩', '😰', '🤥']
emojis_happy = ['😀', '😁', '😃', '😄', '😅', '😉', '🙂', '🤗', '😏', '🙃', '😇']


# check ping command
@bot.command(aliases=['ping', 'checkping'])
async def _ping(ctx):
    await ctx.reply(f"The current ping to the Discord Service is : {round(bot.latency*1000)} ms")


# greet command
@bot.command(aliases=['hi', 'hey', 'hello', 'sup', 'yo'])
async def _greet(ctx):
    await ctx.reply(f"{random.choice(emojis_happy)} \n {random.choice(GREETINGS)}, {ctx.author.name}")


# members join and leave
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention} Welcome to this wonderful server")


@bot.event
async def on_member_leave(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention} Goodbye :( ")


@bot.command()
async def embed(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    name = member.display_name
    pfp = member.display_avatar
    embed = discord.Embed(
        title=f"This is {name} ->", description="Here is what you look like", colour=discord.Colour.random())
    embed.set_author(name=f"{name}")
    embed.set_thumbnail(url=f"{pfp}")
    embed.set_footer(text='Made by Arihant')
    await ctx.send(embed=embed)


bot.run(token)
