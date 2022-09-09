import discord
from discord.ext import commands
from core.classes import cog_E


class rload(cog_E):

    @commands.command()
    async def reload(self,ctx,extension):
        self.bot.reload_extension(F"cmds.{extension}")
        await ctx.send("ok")

def setup(bot):
    bot.add_cog(rload(bot))