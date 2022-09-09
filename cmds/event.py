import discord
from discord.ext import commands
import json
from core.classes import cog_E
import random

with open("setting.json","r",encoding="utf8") as jfile:
    setting_json = json.load(jfile)
with open("json/event.json","r",encoding="utf8") as jfile:
    event_json = json.load(jfile)

keyword_is_msg = event_json["any_msg"] 
keyword_in_msg = event_json["keyword"]

class event(cog_E):
    @commands.Cog.listener()
    async def on_message(self,msg):
        
        if (msg.author != self.bot.user):  #如果不是機器人自己

            print(msg.author,"   ",msg.guild,"   ",msg.content)    #顯示訊息
            for i in keyword_is_msg:
                if msg.content == i :
                    await msg.channel.send(keyword_is_msg[i])
            for i in keyword_in_msg:
                if i in msg.content:
                    await msg.channel.send(keyword_in_msg[i])
            if msg.guild == self.bot.get_guild(827537267908018176):  #學妹群
                if  "學妹" in msg.content:
                    await msg.channel.send("學妹好棒")
        else :
            pass

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        print(error)

def setup(bot):
    bot.add_cog(event(bot))