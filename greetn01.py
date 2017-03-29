import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def greet(self, user : discord.Member):
        """Greets the user tagged, and tells them whether they are busy or not."""

        # Your code will go here
        await self.bot.say("Hello there, " + user.mention + "!")
        if user.status == discord.Status.online :
        	await self.bot.say("You are online.")
        elif user.status == discord.Status.dnd :
        	await self.bot.say("You are busy.")
        elif user.status == discord.Status.idle :
            await self.bot.say("You are idle.")
        else :
            await self.bot.say("You are offline.")
def setup(bot):
    bot.add_cog(Mycog(bot))