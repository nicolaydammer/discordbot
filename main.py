import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    bot = commands.Bot(command_prefix='!')


    @bot.command(name='roll', help='Roll between 1 and 100.')
    async def roll(ctx):
        response = random.randint(1, 100)

        await ctx.send(response)


    @bot.command(name='gamble', help='Gamble with a user defined maximum.')
    async def gamble(ctx, gamble_amount: int):

        if gamble_amount < 1:
            raise discord.DiscordException()
        elif gamble_amount > 50000000:
            raise discord.DiscordException()

        response = random.randint(1, gamble_amount)

        await ctx.send(response)


    @gamble.error
    async def gamble_error(ctx, error):
        response = ""

        if isinstance(error, commands.BadArgument):
            response = "Please pick a number between 1 and 50000000"
        elif isinstance(error, commands.MissingRequiredArgument):
            response = "This command requires you to pick a number between 1 and 50000000"
        elif isinstance(error, discord.DiscordException):
            response = "Your number is either too small or too big, please give a value between 1 and 50000000"

        if response != "":
            await ctx.send(response)


    async def exit_bot():
        await bot.close()


    bot.run(TOKEN)
