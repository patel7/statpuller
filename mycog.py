import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def greet(self, user : discord.Member):
        """This does stuff!"""

        # Your code will go here
        await self.bot.say("Hello there, " + user.mention + "!")

def setup(bot):
    bot.add_cog(Mycog(bot))