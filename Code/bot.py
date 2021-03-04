import discord
from discord.ext import commands
import time
import random
import datetime
import Adafruit_DHT

sensor=Adafruit_DHT.DHT11
gpio=17

TOKEN = 'TOKEN_HIER_PLAATSEN'

description = '''ninjaBot in Python'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    """Says world"""
    #await ctx.send(file=discord.File('my_image.png'))
    await ctx.send(file=discord.File('video.mp4'))

@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@bot.command()
async def meting(ctx):
    """Meet luchtvochtigheid en temperatuur."""
    await ctx.send("De temperatuur en luchtvochtigheid worden gemeten, even geduld. De resultaten worden zodadelijk verstuurd")
    # Use read_retry method. This will retry up to 15 times to
    # get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio) 
    # Reading the DHT11 is very sensitive to timings and occasionally
    # the Pi might fail to get a valid reading. So check if readings are valid.
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        await ctx.send("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print('Ai, er ging iets mis bij het uitvoeren van de meting. Probeer het even opnieuw.')

bot.run(TOKEN)

