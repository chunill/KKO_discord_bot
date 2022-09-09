from re import A
import discord
from discord.ext import commands
import json
import random
from core.classes import cog_E

with open("setting.json","r",encoding="utf8") as jfile:
    setting_json = json.load(jfile)
with open("json/flirt.json","r",encoding="utf8") as jfile:
    flirt = json.load(jfile)

class m(cog_E):
    @commands.command()
    async def 好色喔(self, ctx):
        pic = discord.File(setting_json["pic"])
        await ctx.send(file = pic)
    @commands.command()
    async def 性慾(self, ctx):
        pic = discord.File(setting_json["pic2"])
        await ctx.send(file = pic)
    @commands.command()
    async def yesorno(self, ctx):
        n = random.choice(["yes","no"])
        await ctx.send(n)
    @commands.command()
    async def clean(self, ctx,num:int):
        await ctx.channel.purge(limit=num+1)
    @commands.command()
    async def 狗勾(self,ctx):
        await ctx.send("都來當阿千的狗")
    @commands.command()
    async def flirt(self,ctx):
        k = random.choice(flirt["flirt"])
        await ctx.send(k)
    @commands.command()
    async def fk(self,ctx):
        k = random.choice(flirt["fk"])
        await ctx.send(k)
    @commands.command()
    async def 不可以色色(self,ctx):
        pic = discord.File(setting_json["dog_pic"])
        await ctx.send(file = pic)
    
    @commands.command()
    async def 關於阿千(self,ctx):
        embed=discord.Embed(title="阿千噗浪", url=setting_json["chunill_plurk"], description="機千的本體", color=0x8b16ac)
        embed.set_thumbnail(url="https://i.imgur.com/pERq2xF.jpg")
        embed.add_field(name="關於阿千",value=setting_json["embed_description"], inline=False)
        embed.set_footer(text="log_4")
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self,ctx,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    @commands.command()
    async def says(self,ctx,channel,msg):
        #print(channel[2:-1])
        channel = self.bot.get_channel(int(channel[2:][:-1]))
        #print(msg)
        await channel.send(msg)


def setup(bot):
    bot.add_cog(m(bot))