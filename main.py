from discord.ext import commands
import discord
import time

def get_prefix(client, message):

    prefixes = ['.']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix


    return commands.when_mentioned_or(*prefixes)(client, message)

client = discord.Client()
bot = commands.Bot(                         # 
    command_prefix=get_prefix,              # Nomme le préfix
    description='Bot pour créer des parties personnalisées',  # Description du bot
    owner_id=319511103736512512,            # ID du gérant
    case_insensitive=True                   # La case est sensible ?
)

# case_insensitive=True est utilisé par défaut

cogs = ['cogs.solo', 'cogs.duo', 'cogs.section', 'cogs.soloprivate', 'cogs.duoprivate', 'cogs.sectionprivate', 'cogs.arene', 'cogs.areneprivate', 'cogs.channels', 'cogs.messages', 'cogs.test', 'cogs.roles','cogs.reactions', 'cogs.stats', 'cogs.embed', 'cogs.faq','cogs.automatic', 'cogs.attente']
@bot.event
async def on_ready():                                    # Action dès que le bot s'allume
    print(f'Connecté en tant que {bot.user.name} - {bot.user.id}')  # Donne le nom du bot et son id
    for cog in cogs:
        bot.load_extension(cog)
    return

bot.run('TOKEN DU BOT', bot=True, reconnect=True)
