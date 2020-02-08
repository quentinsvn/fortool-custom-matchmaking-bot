import discord
from discord.ext import commands
import asyncio
import time

class Channels(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # On défini la commande
    @commands.command(
        name='spam',
        description='Anti spam',
    )

    @commands.cooldown(1.0, 10.0, commands.BucketType.guild)
    async def ignore_list(self, ctx):
        try:
            await ctx.channel.send(f"{ctx.author.mention}, commande prise en compte")
        except:
            print("Prout")

def setup(bot):
    bot.add_cog(Channels(bot))