import discord
from discord.ext import commands
import asyncio
import inspect
import time
import os

bot = commands.Bot(command_prefix = "/")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)

def user_is_me(ctx):
    return ctx.message.author.id == "277983178914922497"
	
@bot.command(name='eval', pass_context=True)
@commands.check(user_is_me)
async def _eval(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await bot.say(await res)
    else:
        await bot.delete_message(ctx.message)
        await bot.say(res)

bot.run(os.environ['BOT_TOKEN'])
