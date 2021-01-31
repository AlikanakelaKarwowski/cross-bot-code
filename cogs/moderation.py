import discord, asyncio, sys, os, csv, aiosqlite
from discord.ext import commands
from discord.utils import get

from datetime import date
from key import *


class ModCog(commands.Cog, name='Moderation'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    # Update file when a mod bans someone
    async def ban(self, ctx, member: discord.Member = None, *, reason=""):
        uwu = False
        # User, Moderator, and Server
        mod = ctx.author
        user = await self.bot.fetch_user(member.id)
        server = ctx.guild.name
        if reason == "" or member == None:
            await ctx.send(f"!Ban needs a User and a Reason <@{ctx.author.id}>")
        else:
            # Write to file (appending)
            async with aiosqlite.connect('./ban_list.db ') as db:
                try:
                    print(user)
                    await db.execute("INSERT INTO ban_list (user_id, user_name, reason, date, mod, server) VALUES (?,?,?,?,?,?)", (int(member.id), str(user), str(reason), str(date.today()), str(mod), str(server)))
                    await db.commit()
                except Exception as e:
                    try:
                        with open('/damers-bot/banned_users.txt', mode='a') as csv_file:
                            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            csv_writer.writerow([member.id, user, reason, date.today(), mod, server])
                    except Exception as e:
                        await ctx.send(f"Uh oh, looks like something went wrong. I fucked up.")
                        await ctx.send(f"Send this error \n| {e} |\n to my maintainer <@{dist}>")
                    
                    await ctx.send(f"Uh oh, looks like something went wrong. Dont Worry I Still recorded {user} on the CSV file for you.")
                    await ctx.send(f"Send this error \n| {e} |\n to my maintainer <@{dist}>")

            try:
                embed = discord.Embed(title="Banned", url="" , description="" , color=0xff0000)
                embed.add_field(name="User", value=f"@{user}", inline=True)
                embed.add_field(name="Reason", value=reason, inline=True)
                embed.add_field(name="Moderator", value=f"@{mod}", inline=True)
                embed.add_field(name="Server", value=server, inline=True)
                embed.set_footer(text=f"<{member.id}> @{user}")
                await ctx.send(embed=embed)
            except Exception as e:
                if uwu == True:
                    await ctx.send(f"Wuh Woh Mastew. uwu. Someting Went Aww Fucky Wucky Own Me. uwu. Down't Wowwy Mastew. uwu. I was a godd wittwe bot awnd wecowded {user} fow uwu anyways. uwu")
                    await ctx.send(f"Send this error \n| {e} |\n to my master <@{dist}>")
                else:
                    await ctx.send(f"Uh oh, looks like something went wrong. Dont Worry I Still recorded {user} for you.")
                    await ctx.send(f"Send this error \n| {e} |\n to my maintainer <@{dist}>")

    @commands.command(aliases=["uplist"])
    @commands.has_permissions(administrator=True)
    # Get previous bans pre Bot Inclusion
    async def update_ban_list(self, ctx):
        banned_users = await ctx.guild.bans()
        with open('/damers-bot/banned_users.txt', mode="r") as csv_file:
            data = [i for i in csv.reader(csv_file)]
        w_flag = True
        num = 0
        mod = await self.bot.fetch_user(ctx.author.id)
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

    @commands.command()
    @commands.has_permissions(ban_members=True)
    # Update file when a mod bans someone
    async def retcon(self, ctx, member, *, reason=""):
        uwu = False
        # User, Moderator, and Server
        mod = ctx.author
        try:
            user = await self.bot.fetch_user(int(member))
        except Exception as e:
            await ctx.send(f"Couldnt Find the username for ID:{int(member)}")
            user = "N/A"

        server = ctx.guild.name
        if reason == "":
            await ctx.send(f"!Ban needs a User and a Reason <@{ctx.author.id}>")
        else:
            # Write to file (appending)
            with open('/damers-bot/banned_users.txt', mode='a') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([int(member), user, reason, date.today(), mod, server])
            try:
                embed = discord.Embed(title="Retconned", url="" , description="" , color=0xff0000)
                embed.add_field(name="User", value=f"@{user}", inline=True)
                embed.add_field(name="Reason", value=reason, inline=True)
                embed.add_field(name="Moderator", value=f"@{mod}", inline=True)
                embed.add_field(name="Server", value=server, inline=True)
                embed.set_footer(text=f"<{int(member)}> @{user}")
                await ctx.send(embed=embed)
            except Exception as e:
                if uwu == True:
                    await ctx.send(f"Wuh Woh Mastew. uwu. Someting Went Aww Fucky Wucky Own Me. uwu. Down't Wowwy Mastew. uwu. I was a godd wittwe bot awnd wecowded {user} fow uwu anyways. uwu")
                    await ctx.send(f"Send this error \n| {e} |\n to my master <@{dist}>")
                else:
                    await ctx.send(f"Uh oh, looks like something went wrong. Dont Worry I Still recorded {user} for you.")
                    await ctx.send(f"Send this error \n| {e} |\n to my maintainer <@{dist}>")

def setup(bot):
    bot.add_cog(ModCog(bot))
    print('Moderation Cogs Loaded.')

