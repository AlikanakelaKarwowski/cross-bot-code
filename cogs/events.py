import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import sys
import os
from key import *

class EventsCog(commands.Cog, name='Events'):
    def __init__(self, bot):
        self.bot = bot

    # Clown a Bad Advice User
    @commands.Cog.listener()
    async def on_message(self, ctx):

        if ctx.channel.id in discord_channel:
        # Roles specifically include Bad Advice
            if str(ctx.author.roles).__contains__(role):
                await ctx.add_reaction('🤡')

def setup(bot):
    bot.add_cog(EventsCog(bot))
    print('Events Cogs Loaded.')