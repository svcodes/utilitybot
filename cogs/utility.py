import discord
from discord.ext import commands
from discord import utils
import asyncpg



class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    async def mute(self, ctx, member: discord.Member):
        pass
        

def setup(bot):
    bot.add_cog(Utility(bot))