import discord
from discord.ext import commands

class Reactions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def emoji(self, ctx):
        request = discord.Embed(
            title="Réactions",
            description="Ajout de réactions",
            colour = discord.Colour.blue()
        )
        accept_decline = await ctx.channel.send(embed=request)
        await accept_decline.add_reaction(emoji='\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}')
        await accept_decline.add_reaction(emoji='\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}')
        await accept_decline.add_reaction(emoji='\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}')
        await accept_decline.add_reaction(emoji='\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}')
        await accept_decline.add_reaction(emoji='\N{DIGIT FIVE}\N{COMBINING ENCLOSING KEYCAP}')
        await accept_decline.add_reaction(emoji='\N{DIGIT SIX}\N{COMBINING ENCLOSING KEYCAP}')
        await accept_decline.add_reaction(emoji='\N{DIGIT SIX}\N{COMBINING ENCLOSING KEYCAP}')
        await accept_decline.add_reaction(emoji='\N{DIGIT SIX}\N{COMBINING ENCLOSING KEYCAP}')
        await accept_decline.add_reaction(emoji='\N{CLOUD WITH TORNADO}')
        await accept_decline.add_reaction(emoji='\N{WARNING SIGN}')

def setup(bot):
    bot.add_cog(Reactions(bot))