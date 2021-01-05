#!/usr/bin/python3.8
import csv
from datetime import date
import discord
import os
from key import *
from discord.utils import get
from discord.ext import commands

bot = commands.Bot(command_prefix=['!','.'])

# On Connect
@bot.event
async def on_ready():
    preferences = ['none']
    print(f'{bot.user} has connected to Discord!')

# Clown a Bad Advice User
@bot.event
async def on_message(message):

    if message.channel.id in discord_channel:
	# Roles specifically include Bad Advice
        if str(message.author.roles).__contains__(role):
            await message.add_reaction('🤡')
    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(ban_members=True)
# Update file when a mod bans someone
async def ban(ctx, member: discord.Member = None, *, reason=""):
    if ctx.author
    mod = await bot.fetch_user(ctx.author.id)
    # User, Moderator, and Server
    user = await bot.fetch_user(member.id)
    server = ctx.guild.name
    if reason == "" or member == None:
        await ctx.send(f"!Ban needs a User and a Reason <@{ctx.author.id}>")
    else:
        # Write to file (appending)
        with open('/damers-bot/banned_users.txt', mode='a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([member.id, user, reason, date.today(), mod, server])
        try:
            embed = discord.Embed(title="Banned", url="" , description="" , color=0xff0000)
            embed.add_field(name="User", value=f"@{user}", inline=True)
            embed.add_field(name="Reason", value=reason, inline=True)
            embed.add_field(name="Moderator", value=f"@{mod}", inline=True)
            embed.add_field(name="Server", value=server, inline=True)
            embed.set_footer(text=f"<{member.id}> @{user}")
            await ctx.send(embed=embed)
        except Exception as e:
            if uwu = True:
                await ctx.send(f"Wuh Woh Mastew. uwu. Someting Went Aww Fucky Wucky Own Me. uwu. Down't Wowwy Mastew. uwu. I was a godd wittwe bot awnd wecowded {user} fow uwu anyways. uwu")
                await ctx.send(f"Send this error \n| {e} |\n to my master <@{dist}>")
            else:
                await ctx.send(f"Uh oh, looks like something went wrong. Dont Worry I Still recorded {user} for you.")
                await ctx.send(f"Send this error \n| {e} |\n to my maintainer <@{dist}>")

@bot.command(aliases=["uplist"])
@commands.has_permissions(administrator=True)
# Get previous bans pre Bot Inclusion
async def update_ban_list(ctx):
    banned_users = await ctx.guild.bans()
    with open('/damers-bot/banned_users.txt', mode="r") as csv_file:
        data = [i for i in csv.reader(csv_file)]
    w_flag = True
    num = 0
    mod = await bot.fetch_user(ctx.author.id)
    for entry in banned_users:
        DID = entry.user.id
        reason = entry.reason
        if reason =="":
            reason = "None"
        for row in data:
            if row[0] == str(DID):
                w_flag = False
        if w_flag == True:
             with open('/damers-bot/banned_users.txt', 'a') as csv_file:
                 csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                 csv_writer.writerow([DID, entry.user, reason, "Date N/A", mod, ctx.guild.name])
             print(f"Added Entry for user {entry.user}")
             num += 1
    await ctx.send(f"Updated List with {num} Entries")

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
            embed = discord.Embed(title="Banned", url="",
                                  description="", color=0xff0000)
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
