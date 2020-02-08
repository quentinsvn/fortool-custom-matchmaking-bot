import discord
from discord.ext import commands

class Faq(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='faq',
        description='Aide pour les débiles',
    )

    async def faq(self, ctx, arg = None):
        if(arg == 'htbp'):
            htbp = discord.Embed(
                    title='Comment devenir premium ?',
                    description="Pour obtenir le grade premium, il suffit que 10 personnes rejoignent le serveur avec votre lien d'invitation discord",
                    colour = discord.Colour.blue()
                )
            await ctx.channel.send(embed=htbp)
        elif(arg == 'help'):
            help = discord.Embed(
                    title='Listes des commandes',
                    colour = discord.Colour.blue()
                )
            help.add_field(name="htbp", value="Comment devenir premium ?", inline=False)
            help.add_field(name="ap", value="Quels sont les avantages du premium ?", inline=False)
            help.add_field(name="valid", value="Comment se faire valider ?", inline=False)
            help.add_field(name="read_bot", value="Pourquoi je ne peux pas écrire dans les salons des bots ?", inline=False)
            help.add_field(name="partner", value="Comment devenir partenaire ?", inline=False)
            help.add_field(name="partner_benefits", value="Quels sont les avantages d'un partenaire ?", inline=False)
            help.add_field(name="info_bot", value="Est-il possible d'avoir les bots pp sur mon serveur ?", inline=False)
            await ctx.channel.send(embed=help)
        elif(arg == 'ap'):
            ap = discord.Embed(
                    title="Quels sont les avantages du premium ?",
                    description="Les fonctionnalités du grade premium sont les suivantes:",
                    colour = discord.Colour.blue()
                )
            ap.add_field(name="▪️ Donne accès à des codes de PP personnalisable.", value="---------------------------------------------------------------------")
            ap.add_field(name="▪️ Réduit le  temps d'attente pour recréer une PP.", value="---------------------------------------------------------------------")
            ap.add_field(name="▪️ Donne accès à des channels textuel confidentiels.", value="---------------------------------------------------------------------")
            ap.add_field(name="▪️ Permet de creer des parties personnalisées privés (vous recevrez le mot de passe en message privé)", value="---------------------------------------------------------------------")
            ap.add_field(name="▪️ Donne accès aux modes temporaires avec les commandes: (.pptemp/.pptempp et .pp2temp/.pp2tempp)", value="---------------------------------------------------------------------")
            await ctx.channel.send(embed=ap)
        elif(arg == 'valid'):
            valid = discord.Embed(
                    title="Comment se faire valider ?",
                    description="Pour ce faire validé, envoyé un screen ou une photo de la boutique Fortnite avec le code créateur 'Fortool' dans le salon <#578618904830541855>",
                    colour = discord.Colour.blue()
                )
            await ctx.channel.send(embed=valid)
        elif(arg == 'read_bot'):
            bot = discord.Embed(
                    title="Pourquoi je ne peux pas écrire dans les salons des bots ?",
                    description="Si vous ne parvenez pas à écrire dans <#578618765449887772>/<#585752511093145601> attentez que l'émoticône ✅ apparaisse dans les **noms des salons** suivi du message '__Le système est à présent opérationnel !__' pour pouvoir lancer une partie personnalisée (**il faut être rapide**)",
                    colour = discord.Colour.blue()
                )
            await ctx.channel.send(embed=bot)
        elif(arg == 'partner'):
            partner = discord.Embed(
                    title="Comment devenir partenaire",
                    description="Pour devenir partenaire youtube vous devez posséder un minimum de **300 abonnés** ainsi que **10 000 vues** au total sur votre chaîne. Une **vidéo de présentation** du serveur sera également nécessaire.",
                    colour = discord.Colour.blue()
                )
            await ctx.channel.send(embed=partner)
        elif(arg == 'partner_benefits'):
            partner_benefits = discord.Embed(
                    title="Quels sont les avantages d'un partenaire ?",
                    description="Les partenaires peuvent partager leurs vidéos depuis le salon <#585139974559498281> et ainsi augmenter leur audience !",
                    colour = discord.Colour.blue()
                )
            await ctx.channel.send(embed=partner_benefits)
        elif(arg == 'info_bot'):
            info_bot = discord.Embed(
                    title="Est-il possible d'avoir les bots pp sur mon serveur ?",
                    description="**Non**, les Bots (étant développé par nos soins) sont **uniquement disponibles sur Fortool** et nul par ailleurs !",
                    colour = discord.Colour.blue()
                )
            await ctx.channel.send(embed=info_bot)
        else:
            await ctx.channel.send(f"{ctx.author.mention}, Veuillez spécifiez le problème !")

def setup(bot):
    bot.add_cog(Faq(bot))