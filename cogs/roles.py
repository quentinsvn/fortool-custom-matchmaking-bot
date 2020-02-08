import discord
from discord.ext import commands
import asyncio

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # On défini la commande
    @commands.command(
        name='roles',
        description='Ajout/suppresion de roles',
    )

    @commands.Cog.listener()
    async def roles(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name="10 min")
        user = ctx.message.author
        await user.add_roles(role)
        await ctx.channel.send('Votre rôle à était ajouté')
        await asyncio.sleep(10)
        await ctx.channel.send('Votre rôle à était supprimé')
        await user.remove_roles(role)

def setup(bot):
    bot.add_cog(Roles(bot))