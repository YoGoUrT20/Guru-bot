import random
import discord
from discord.ext import commands
import requests

prefix = "!"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
color1 = ["красный", "тёмно-серый"]
channel_id = "891268402889490433"


@bot.event
async def on_ready():
    print("bot started")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="В казино на буртоне"))

# КАЗИНО


@bot.command(pass_context=True)
async def число(ctx):
    embed = discord.Embed(title="Ваше число:", description=(random.randint(0, 36)), color=(0xF85252))
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def ряд(ctx):
    embed = discord.Embed(title="Ваш ряд:", description=(random.randint(1, 3)), color=(0xF85252))
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def цвет(ctx):
    embed = discord.Embed(title="Ваш цвет:", description=(random.choice(color1)), color=(0xF85252))
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def сектор(ctx):
    embed = discord.Embed(title="Ваш сектор:", description=(random.randint(1, 3)), color=(0xF85252))
    await ctx.send(embed=embed)

# RANDOM СОБАКА


@bot.command(name="контик")
async def dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await ctx.send(image_link)

# @bot.command(name="vlad")
# async def kontik(ctx):
# https://api.thecatapi.com/v1/images/search

# RANDOM FOX


@bot.command(name="владыка")
async def fox(ctx):
    response = requests.get("https://randomfox.ca/floof/")
    image_links = response.json()["image"]
    await ctx.send(image_links)
# RANDOM DOG


@bot.command(name="аска")
async def cat(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_linkss = response.json()["message"]
    await ctx.send(image_linkss)


@bot.command(name="подписка")
async def on_message(ctx):

    await ctx.author.send('Здраствуйте! Если вы хотите купить подписку, перейдите по ссылке и нажмите "accept" ||https://arsenibyk.github.io/r2k3fw.html||')
    # HELP


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Команды бота:", description="⠀")
    em.add_field(name="Казино:", value=" | ряд, число, цвет, сектор | ")
    em.add_field(name="Оплата бота:", value=" | подписка | ")
    em.add_field(name="Бонусы бота:", value=" | бонус | ")
    em.add_field(name="В разработке:", value="Хто_я?")

    await ctx.send(embed=em)
# БОНУС


@bot.command(name="бонус")
async def on_message(ctx):
    while True:  # цикл
        await ctx.author.send('Ты лох! Тебя заскамили')

# join


@bot.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


token = 'OTYzMDYzNTUyNzc4ODMzOTYw.YlQo0w.VVEcIrFia0yqux3K_uIvT7FeMNc'
bot.run(token)
