import discord
from discord.ext import commands
import dotenv
import os


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="p!", intents=intents)


if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    token = os.environ["BOT_TOKEN"]

    COGS = [
        "cogs.%s" % os.path.splitext(COG_NAME)[0] for COG_NAME in os.listdir("./cogs")
        if os.path.splitext(COG_NAME)[1] == ".py"
    ]

    for cog in COGS:
        bot.load_extension(cog)

    bot.run(token)
