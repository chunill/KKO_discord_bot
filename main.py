import discord
from discord.ext import commands
import json
import os


intents = discord.Intents.all()
discord.members = True
bot = commands.Bot(command_prefix='>',intents = intents)

with open("setting.json","r",encoding="utf8") as jfile:
    setting_json = json.load(jfile)


@bot.event
async def on_ready():
    print("Bot is online")


for F in os.listdir("./cmds"):
    if F.endswith(".py"):
        #test
        bot.load_extension(f"cmds.{F[:-3]}")

if __name__ == "__main__":
    bot.run(setting_json["TOKEN"])
