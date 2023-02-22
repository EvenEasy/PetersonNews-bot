import config, discord
from discord.ext import commands

bot = commands.Bot('$', intents=discord.Intents.all())
tree = bot.tree