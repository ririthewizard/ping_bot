import discord
from dotenv import load_dotenv
import os
import random

load_dotenv()
TOKEN = str(os.getenv("TOKEN"))

bot = discord.Bot()



@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[1303445508840493156])
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hello!")

@bot.slash_command(guild_ids=[1303445508840493156])
async def gtn(ctx: discord.ApplicationContext):
    await ctx.respond("Guess a number between 1 and 69")
    guess = await bot.wait_for("message", check=lambda message: message.author == ctx.author)

    if int(guess.content) == 5:
        await ctx.send("You guessed it, hooray!")
    else:
        await ctx.send("NOPE, try again.")


bot.run(f"{TOKEN}")


