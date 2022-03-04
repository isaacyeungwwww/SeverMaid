import discord
from discord.ext import commands

bot = commands.bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('7b081d4ef81d58dad06d37db7cc5b6726884daa23d1ba64748c1ae655e040904')