import os
import discord
import asyncio
import aiohttp
from discord.ext import commands
from redbot.core import checks

class AddShit:
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @checks.is_owner()
    @commands.command(hidden=True, pass_context=True)
    async def addshit(self, ctx):
        """Add an image to direct upload."""
        channel = ctx.message.channel
        msg = ctx.message
        directory = "/home/ftwtech/guaccogs/shitpost/data/"
        async with self.session.get(msg.attachments[0].url) as resp:
            test = await resp.read()
            with open(file_path, "wb") as f:
                f.write(test)
        await ctx.send("added")