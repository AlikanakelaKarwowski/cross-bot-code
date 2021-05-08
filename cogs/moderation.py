import discord, asyncio, sys, os, csv, aiosqlite
from discord.ext import commands
from discord.utils import get

from datetime import date
from key import *
import time

# General db insert for bans
async def db_ban(ctx, mem_id, user, reason, mod, server ):
    async with aiosqlite.connect('/cross-bot-code/ban_list.db') as db:
        try:
            await db.execute("INSERT OR IGNORE INTO ban_list(user_id, user_name, reason, date, mod, server) VALUES(?, ?, ?, ?, ?, ?)",
                (int(mem_id), str(user), str(reason), str(date.today()), str(mod), str(server)))
            await db.commit()
        except Exception as e:
            try:
                with open('/damers-bot/banned_users.txt', mode='a') as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow([mem_id, user, reason, date.today(), mod, server])
            except Exception as EX:
                await ctx.send(f"Uh oh, looks like something went wrong. I fucked up.")
                await ctx.send(f"Send this error \n| {EX} |\n to my maintainer <@{dist}>")
            
            await ctx.send(f"Uh oh, looks like something went wrong. Dont Worry I Still recorded {user} on the CSV file for you.")
            await ctx.send(f"Send this error \n| {e} |\n to my maintainer <@{dist}>")
class ModCog(commands.Cog, name='Moderation'):

    def __init__(self, bot):
        self.bot = bot

    # Update file when a mod bans someone
    @commands.command()
    async def ban(self, ctx, member: discord.Member = None, *, reason=""):
        mod = ctx.author
        perms = mod.guild_permissions.ban_members
        mod_r= False
        for r in mod_roles:
            if r in str(mod.roles):
                mod_r =True
        if perms or mod_r:
            # User, Moderator, and Server
            user = await self.bot.fetch_user(member.id)
            server = ctx.guild.name
            if reason == "" or member == None:
                await ctx.send(f"!Ban needs a User and a Reason <@{ctx.author.id}>")
            else:
                await db_ban(ctx, member.id, user, reason, mod, server)
                try:
                    embed = discord.Embed(title="Banned", url="" , description="" , color=0xff0000)
                    embed.add_field(name="User", value=f"@{user}", inline=True)
                    embed.add_field(name="Reason", value=reason, inline=True)
                    embed.add_field(name="Moderator", value=f"@{mod}", inline=True)
                    embed.add_field(name="Server", value=server, inline=True)
                    embed.set_footer(text=f"<{member.id}> @{user}")
                    await ctx.send(embed=embed)
                except Exception as e:
                    await ctx.send(f"Uh oh, looks like something went wrong. Dont Worry I Still recorded {user} for you.")
                    await ctx.send(f"Send this error \n| {e} |\n to my maintainer <@{dist}>")
        else:
            await ctx.send(f"You don't have the right perms or roles. If you think this is an error please contact your admins about it.")

    
    # Get previous bans pre Bot Inclusion
    # bot must have ban permissions to run
    @commands.command(aliases=["uplist"])
    async def update_ban_list(self, ctx):
        mod = ctx.author
        perms = mod.guild_permissions.ban_members
        server = ctx.guild.name
        if perms:
            try:
                banned_users = await ctx.guild.bans()
                num = 0
                for entry in banned_users:
                    reason = entry.reason
                    if reason == "":
                        reason = "None"
                    await db_ban(ctx, entry.user.id, entry.user, reason, mod, server)
                    num += 1
            
            except Exception as e:
                await ctx.send(f"If your seeing this message then the bot most likely doesnt have the right permissions. It needs the \"Ban Users\" permission enabled.")
                
            await ctx.send(f"Updated List with {num} Entries")
                    # try:
                    #     await db.execute("""
                    #         INSERT OR IGNORE INTO ban_list(user_id, user_name, reason, date, mod, server)
                    #         VALUES(?,?,?,?,?,?)""",
                    #         (
                    #             int(entry.user.id), str(entry.user), str(reason),
                    #             str(date.today()), str(ctx.author), str(ctx.guild.name)
                    #         )
                    #     )
                    # except Exception as e:
                    #     await ctx.send(f"Send this error \n| {e} |\n to my maintainer <@{dist}>")
                # await db.commit()

    # Update file when a mod bans someone
    @commands.command()
    @commands.has_permissions(ban_members=True)
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

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def autoban(self, ctx, *members):
            #await ctx.send("Disabled, message Shin Ma#2121 to reenable")
            reason = "bot or raid, if you feel this is an error message Shin Ma#2121"
            server = ctx.guild.name
            mod = ctx.author
            for member in members:
                try:
                    member = await bot.fetch_user(int(member))
                    await ctx.send(f"!ban {member} bot or raid")
                    await ctx.guild.ban(member, reason=reason)
                    await db_ban(ctx, member.id, member, reason, mod, server)
                    time.sleep(1)
                except Exception as e:
                    ctx.send(f"The following error occured \n {e} \n Please message the creator for help")

def setup(bot):
    bot.add_cog(ModCog(bot))
    print('Moderation Cogs Loaded.')

