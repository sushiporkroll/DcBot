import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import inspect
import time
import os

bot = commands.Bot(command_prefix = "/")

@bot.event
async def on_ready():
    print("Bot is in my penis!")

def user_is_me(ctx):
    return ctx.message.author.id == "303657894161809412"

@bot.command(name='eval', pass_context=True)
@commands.check(user_is_me)
async def _eval(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await bot.say(await res)
    else:
        await bot.say(res)

bot.run(os.environ['BOT_TOKEN'])
