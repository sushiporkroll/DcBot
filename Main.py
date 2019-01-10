import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    print("Bot is in my penis!")

def user_is_me(ctx):
    return ctx.message.author.id == "303657894161809412"

@client.command(name='eval', pass_context=True)
@commands.check(user_is_me)
async def _eval(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await client.say(await res)
    else:
        await client.say(res)

client.run(os.environ['BOT_TOKEN'])
