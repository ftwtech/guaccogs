import discord

class Qtemp:
    """qtemp"""

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        guild = message.guild
        channel = message.channel
        role = "".join(role.mention for role in guild.roles if role.name == "QPOSTS")
        if "New Q Post!" in message.content.lower():
            await channel.send("{}".format(role.mention))
def setup(bot):
    bot.add_cog(Qtemp(bot))