import discord
import os
from discord.ext.commands import Bot

bot = Bot(command_prefix = '!')

token = os.environ['TOKEN']

@bot.event
async def on_message(msg):
    await bot.process_commands(msg)
    # ignore messages sent by bot
    if msg.author == bot.user:
        return

    await msg.add_reaction(f'⬆')
    await msg.add_reaction(f'⬇')

bot.run(token)