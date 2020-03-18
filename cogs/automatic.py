import discord
from discord.ext import commands
import os
import random
import string
from pynput.keyboard import Key, Controller
import subprocess
import time
import asyncio

class Solo(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    # On défini la commande
    @commands.command(
        name='automatic',
        description='Mode automatique',
    )

    @commands.cooldown(1, 30, commands.BucketType.guild)
    async def solo_command(self, ctx):
        client = commands.Bot(command_prefix = '.')
        id = client.get_guild(578618765449887772)
        if "✅ valid" in [role.name for role in ctx.author.roles]:
            channels = ["mode-automatique┆bot-1"]
            role = ctx.guild.default_role
            while True:
                await ctx.channel.set_permissions(role, send_messages=False, read_messages=True, read_message_history=True, mention_everyone=False)
                if str(ctx.channel) in channels:
                    response = random.choice(["Solo", "Duo", "Section", "Arene solo"])
                    if(response == "Solo"):
                        command = "macro-shadow/solo-1.exe"
                        #subprocess.Popen(command)
                    elif(response == "Duo"):
                        command = "macro-shadow/duo-1.exe"
                        #subprocess.Popen(command)
                    elif(response == "Section"):
                        command = "macro-shadow/section-1.exe"
                        #subprocess.Popen(command)
                    elif(response == "Arene solo"):
                        command = "macro-shadow/soloarene-1.exe"
                        #subprocess.Popen(command)
                    await asyncio.sleep(14)
                    keyboard = Controller()
                    randomcode = random.randint(1000, 9999)
                    for char in f"ft{randomcode}":
                        keyboard.press(char)
                        keyboard.release(char)
                    request = discord.Embed(
                        title=f"Code: ft{randomcode}",
                        colour = discord.Colour.blue()
                    )
                    if(response == "Solo"):
                        start = "macro-shadow/solo-2.exe"
                        #subprocess.Popen(start)
                    elif(response == "Duo"):
                        start = "macro-shadow/duo-2.exe"
                        #subprocess.Popen(start)
                    elif(response == "Section"):
                        start = "macro-shadow/section-2.exe"
                        #subprocess.Popen(start)
                    elif(response == "Arene solo"):
                        start = "macro-shadow/soloarene-2.exe"
                        #subprocess.Popen(start)
                    request.add_field(name=f'Mode: {response}', value=':flag_fr: Vous avez 2 minutes pour rejoindre la partie!')
                    request.add_field(name=f"Mode: {response}", value=':flag_gb: You have 2 minutes to join the game!')
                    request.set_footer(text='©Fortool - discord.me/fortool')
                    await asyncio.sleep(7)
                    await ctx.channel.send(embed=request)
                    await asyncio.sleep(128)
                    ready = "macro-shadow/ready.exe"
                    #subprocess.Popen(ready)
                    finish = discord.Embed(
                        title="Mode automatique",
                        colour = discord.Colour.green()
                    )
                    finish.add_field(name=":flag_fr: Création d'une nouvelle partie en cours... !", value=":flag_gb: Creating a new game in progress...!")
                    await ctx.channel.send(embed=finish)
                    await asyncio.sleep(50)
                    await ctx.channel.set_permissions(role,send_messages=False, read_messages=True, read_message_history=True, mention_everyone=False)
                else:
                    await ctx.channel.send(f"{ctx.author.mention}, Les parties personnalisées ne peuvent qu'être lancées dans le salon <#578618765449887772> !")
        else: 
            await ctx.channel.send(":white_check_mark: Vous devez être validé pour pouvoir utiliser cette commande. Pour en savoir plus rendez-vous dans le salon <#578618904830541855>")


def setup(bot):
    bot.add_cog(Solo(bot))
