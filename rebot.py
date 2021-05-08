#!/usr/bin/python3.8
import discord, sys, asyncio, os
import random as rd
from discord.utils import get
from discord.ext import commands
from key import *

#intents = discord.Intents.default()
#intents.members = True
bot = commands.Bot(command_prefix=['!','.'])
# On Connect
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
semen = 0
initial_extensions = ['cogs.moderation', 'cogs.events']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong {round(bot.latency*1000)}ms")

@bot.command()
@commands.has_any_role('Staff','Experienced Builder','Helper (Jr. EB)','Nitro Booster')
async def ding(ctx, unit="inch"):
    global semen
    rd.seed((ctx.author.id + semen))
    if ctx.author.id == dist:
       await ctx.send(f"Your Dong is {rd.randrange(75,100)/10} inches long")
    elif unit == "cm" or unit == "CM" or unit == "Cm" :
        await ctx.send(f"Your Dong is {round(rd.randrange(50,100)/10*2.54, 1)} cm long")
    else:
        await ctx.send(f"Your Dong is {rd.randrange(50,100)/10} inches long")

@bot.command()
async def seedgen(ctx, amount=0):
    global semen
    if ctx.author.id == dist:
        semen += int(amount)
        await ctx.send(f"Seed was updated for new month by {amount} amount")

@bot.command()
async def dong(ctx, member: discord.Member):
    rd.seed(member.id)
    if ctx.author.id == dist:
        await ctx.send(f"{member.name}'s Dong is {round(rd.randrange(0,100)/10 - 3, 1)} inches long")
    else:
        return None


bot.run(DISCORD_TOKEN)
