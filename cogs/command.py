import discord
from discord.ext import commands


class Command(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[ BOT ] {self.bot.user.name} is ready")

    @commands.slash_command(name="hello")
    async def hello_command(self, interaction: discord.Interaction):
        text = "Hello %s" % interaction.user.mention
        await interaction.response.send_message(content=text)

    @commands.slash_command(name="button")
    async def button_demo(self, interaction: discord.Interaction):
        # https://youtu.be/kNUuYEWGOxA
        pass

    @commands.slash_command(name="select")
    async def button_demo(self, interaction: discord.Interaction):
        # https://youtu.be/56XoybDajjA
        pass


def setup(bot: discord.Bot):
    return bot.add_cog(Command(bot))