import os
import discord
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    discord_client = discord.Client()

    @discord_client.event
    async def on_ready():
        print(f'{discord_client.user} has connected to discord!')

    discord_client.run(TOKEN)
