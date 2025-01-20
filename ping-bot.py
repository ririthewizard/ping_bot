import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

load_dotenv()
TOKEN = os.getenv("TOKEN") #TODO: Figure out if bot.run(os.getenv(f"{TOKEN})) ? bot.run(f"{TOKEN})

description = """A bot that can ping you for events you create"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description = description,
    intents = intents,
) 



@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(name="guess", description="Guess a number between 1 and 69!")
async def gtn(ctx: discord.ApplicationContext):
    await ctx.respond("Guess a number between 1 and 69.")

    def is_valid_guess(m: discord.Message):
        return (
            m.author == ctx.author and m.content.isdigit() and 1 <= (m.content) < 70
        )

    answer = random.randint(1,69)

    try:
        guess: discord.Message = await bot.wait_for("message", check=is_valid_guess, timeout=5.0)
    except TimeoutError:
        return await ctx.send_followup(f"Sorry, you took to long, the answer is {answer}")

    if int(guess.content) == answer:
        await guess.reply("You are right!", mention_author=True)
    else:
        await guess.reply(f"Oops, the answer was actually {answer}")

bot.run(f"{TOKEN}")


