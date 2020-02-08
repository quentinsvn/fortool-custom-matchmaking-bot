import discord
from discord.ext import commands
import asyncio

class Slowmode(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # On défini la commande
    @commands.command(
        name='slowmode',
        description='Modification du titre',
    )

    @commands.Cog.listener()
    async def slowmode(self, ctx):
        await ctx.channel.edit(slowmode_delay='1200')
        await ctx.channel.send('Slowmode activé')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('.sm'):
            await message.channel.set_permissions(message.author, read_messages=True, send_messages=False)
            await message.channel.send(f"{message.author.mention}, Permissions modifiés")
            await asyncio.sleep(20)
            await message.channel.set_permissions(message.author, read_messages=True, send_messages=True)
            await message.channel.send(f"{message.author.mention}, Permissions remodifiés")


def setup(bot):
    bot.add_cog(Slowmode(bot))