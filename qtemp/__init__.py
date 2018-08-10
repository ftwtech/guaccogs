from .qtemp import Qtemp

def setup(bot):
    n = Qtemp(bot)
    bot.add_cog(n)