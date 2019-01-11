import discord
from discord.ext import commands
import asyncio
import time
import os
import inspect

bot = commands.Bot(command_prefix = "/")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)

def user_is_me(ctx):
	return ctx.message.author.id == "277983178914922497", "303657894161809412"

@bot.command(name='eval', pass_context=True)
@commands.check(user_is_me)
async def _eval(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await bot.say(await res)
    else:
    	await bot.say(res)
	
@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("{}".format(ctx.message.author.mention))

bot.run(os.environ['BOT_TOKEN'])
