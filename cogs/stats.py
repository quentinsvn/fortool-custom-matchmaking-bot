import discord
from discord.ext import commands
from ray import Reader

class Stats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def stats(self, ctx):
        with Reader("C:/Users/Quentin SAVEAN/AppData/Local/FortniteGame/Saved/Demos/UnsavedReplay-2019.06.30-13.59.12.replay") as replay:
            for elim in replay.eliminations:
                await ctx.channel.send(elim)

def setup(bot):
    bot.add_cog(Stats(bot))