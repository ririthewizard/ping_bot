import discord
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[1303445508840493156])
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hello!")

bot.run(f"{TOKEN}")