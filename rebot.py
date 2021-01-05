#!/usr/bin/python3.8
import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import sys
import os
import csv
from datetime import date
from key import *

bot = commands.Bot(command_prefix=['!','.'])

# On Connect
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

initial_extensions = ['cogs.moderation']

if __name__ == '__main__':
    for extension in initial_extenstions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}")
            traceback.print_exc()

            
# Clown a Bad Advice User
@bot.event
async def on_message(message):

    if message.channel.id in discord_channel:
	# Roles specifically include Bad Advice
        if str(message.author.roles).__contains__(role):
            await message.add_reaction('🤡')
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong {round(bot.latency*1000)}ms")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, *, reason=""):
    user = await bot.fetch_user(member.id)
    mod = await bot.fetch_user(ctx.author.id)
    server = ctx.guild.name
    if reason == "" or member == None:
        await ctx.send(f"!Unban needs a User and a Reason <@{ctx.author.id}>")
    else:
        # Write to file (appending)
        with open('/damers-bot/banned_users.txt', mode='r+') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[0] == member.id and row[5] == ctx.guild.name:
                    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow

                

        try:
            embed = discord.Embed(title="Banned", url="", description="", color=0xff0000)
            embed.add_field(name="User", value=f"@{user}", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Moderator", value=f"@{mod}", inline=True)
            embed.add_field(name="Server", value=server, inline=True)
            embed.set_footer(text=f"<{member.id}> @{user}")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"Wuh Woh Mastew. uwu. Someting Went Aww Fucky Wucky Own Me. uwu. Down't Wowwy Mastew. uwu. I was a godd wittwe bot awnd wecowded {user} fow uwu anyways. uwu")
            await ctx.send(f"Send this error | {e} | to my master <@{dist}>")


bot.run(DISCORD_TOKEN)
