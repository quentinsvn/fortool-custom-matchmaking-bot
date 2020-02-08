import discord
from discord.ext import commands

class Attente(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def _make_member(self, server, data):
        roles = [server.default_role]
        for roleid in data.get('roles', []):
            role = utils.get(server.roles, id=roleid)
            if role is not None:
                roles.append(role)

        data['roles'] = sorted(roles)
        return Member(server=server, **data)
        

def setup(bot):
    bot.add_cog(Attente(bot))