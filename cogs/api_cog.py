# for interaction commands

import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
import requests
import random


class api_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("cog : api_cog.py has been loaded")

    @commands.command(aliases=['dog', 'doggy', 'doggo', 'puppy', 'pup'])
    async def _dog(self, ctx):
        r = requests.get("https://dog.ceo/api/breeds/image/random")
        res = r.json()
        em = discord.Embed()
        em.set_image(url=res['message'])
        await ctx.send(embed=em)

    @commands.command(aliases=['wouldyourather', 'wyr'])
    async def _wyr(self, ctx):
        r = requests.get("https://api.truthordarebot.xyz/v1/wyr")
        res = r.json()
        await ctx.send(res['question'])

    @commands.command(aliases=['truth'])
    async def _truth(self, ctx):
        r = requests.get("https://api.truthordarebot.xyz/v1/truth")
        res = r.json()
        await ctx.send(res['question'])

    @commands.command(aliases=['dare'])
    async def _dare(self, ctx):
        r = requests.get("https://api.truthordarebot.xyz/v1/dare")
        res = r.json()
        await ctx.send(res['question'])

    @commands.command(aliases=['kanye', 'kanyequote', 'ye', 'yezus', 'yequote'])
    async def _kanye(self, ctx):
        r = requests.get("https://api.kanye.rest")
        res = r.json()
        response = res['quote']
        await ctx.send(f'**Kanye says :**  {response}')


async def setup(bot):
    await bot.add_cog(api_cog(bot))
