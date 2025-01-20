import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

load_dotenv()
#TOKEN = os.getenv("TOKEN") TODO: Figure out if bot.run(os.getenv(f"{TOKEN})) ? bot.run(f"{TOKEN})

description = """A bot that can ping you for events you create"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    description = description,
    intents = intents,
) 



@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command(description="For when you wanna settle the score some other way")
async def choose(ctx: commands.Context, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

#@bot.command()
#async def gtn(ctx):
#    """A Slash Command to play a Guess-the-Number game."""
#
#    await ctx.respond('Guess a number between 1 and 10.')
#    guess = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
#
#    if int(guess.content) == 5:
#        await ctx.send('You guessed it!')
#    else:
#        await ctx.send('Nope, try again.')


bot.run(os.getenv("TOKEN"))


