import discord
from discord.ext import commands

class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joined(self, member : discord.Member):
        await self.bot.send('{0.name} joined in {0.joined_at}'.format(member))

    @commands.group(pass_context=True)
    async def cool(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.send('No, {0.subcommand_passed} is not cool'.format(ctx))

    @cool.command(name='bot')
    async def _bot(self):
        await self.bot.channel.send('Yes, the bot is cool.')


def setup(bot):
    bot.add_cog(Members(bot))