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
        name='ppsolo',
        description='Mode solo',
    )

    @commands.cooldown(1, 30, commands.BucketType.channel)
    async def solo_command(self, ctx):
        client = commands.Bot(command_prefix = '.')
        id = client.get_guild(578618765449887772)
        if "✅ valid" in [role.name for role in ctx.author.roles]:
            channels = ["✅┆bot-1"]
            role = ctx.guild.default_role
            await ctx.channel.set_permissions(role, send_messages=False, read_messages=True, read_message_history=True, mention_everyone=False)
            if str(ctx.channel) in channels:
                embed = discord.Embed(
                    description=f"{ctx.author.mention}",
                    colour = discord.Colour.green()
                )
                embed.add_field(name="Création en cours", value=':flag_fr: Votre partie personnalisée est en cours de création...')
                embed.add_field(name="Creation in progress", value=":flag_gb: Your custom game is being created ...")
                await ctx.channel.send(embed=embed)
                command = "C:/Users/Quentin SAVEAN/Desktop/python/macro-shadow/solo-1.exe"
                #subprocess.Popen(command)
                await asyncio.sleep(14)
                keyboard = Controller()
                randomcode = random.randint(1000, 9999)
                for char in f"{randomcode}":
                    keyboard.press(char)
                    keyboard.release(char)
                request = discord.Embed(
                    title=f"Code: {randomcode}",
                    colour = discord.Colour.blue()
                )
                start = "C:/Users/Quentin SAVEAN/Desktop/python/macro-shadow/solo-2.exe"
                #subprocess.Popen(start)
                request.add_field(name='Mode: Solo', value=':flag_fr: Vous avez 2 minutes pour rejoindre la partie!')
                request.add_field(name="Mode: Solo", value=':flag_gb: You have 2 minutes to join the party!')
                request.set_footer(text='©Fortool - discord.me/fortool')
                await asyncio.sleep(7)
                await ctx.channel.send(embed=request)
                await asyncio.sleep(128)
                ready = "C:/Users/Quentin SAVEAN/Desktop/python/macro-shadow/ready.exe"
                #subprocess.Popen(ready)
                finish = discord.Embed(
                    description=f"{ctx.author.mention}",
                    colour = discord.Colour.green()
                )
                finish.add_field(name=":flag_fr: Votre partie personnalisée est désormais en cours !", value=":flag_gb: The custom party is now in progress!")
                await ctx.channel.send(embed=finish)
                await asyncio.sleep(50)
                operational = discord.Embed(
                    title=":flag_fr: Le système est à présent opérationnel !",
                    description=":flag_gb: The system is now operational !",
                    colour = discord.Colour.red()
                )
                await ctx.channel.send(embed=operational)
                await ctx.channel.set_permissions(role,send_messages=True, read_messages=True, read_message_history=True, mention_everyone=False)
            else:
                await ctx.channel.send(f"{ctx.author.mention}, Les parties personnalisées ne peuvent qu'être lancées dans le salon <#578618765449887772> !")
        else: 
            await ctx.channel.send(":white_check_mark: Vous devez être validé pour pouvoir utiliser cette commande. Pour en savoir plus rendez-vous dans le salon <#578618904830541855>")


def setup(bot):
    bot.add_cog(Solo(bot))