import os
import discord
import asyncio
from discord.ext import commands
from redbot.core import checks

class AddShit:
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(hidden=True, pass_context=True)
    async def addshit(self, ctx, cmd):
        """Add an image to direct upload."""
        channel = ctx.message.channel
        msg = ctx.message
        await ctx.send("Upload an image for me to use, type `exit` to cancel")
        while msg is not None:
            check = lambda msg.attachments != []
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=60)
            except asyncio.TimeoutError:
                await ctx.send("Image adding timed out.")
                break

            else:
                filename = "{}".format(msg.attachments.filename)
                
                directory = "/home/ftwtech/guaccogs/shitpost/data/"
                async with self.session.get(msg.attachments[0].url) as resp:
                    test = await resp.read()
                    with open(file_path, "wb") as f:
                        f.write(test)
                await self.config.images.set(global_imgs)
                await ctx.send("added")
                break
            if msg.content.lower().strip() == "exit":
                await ctx.send("Image adding cancelled.")
                break