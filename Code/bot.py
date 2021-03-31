import discord
from discord.ext import commands
import time
import random
import datetime
import RPi.GPIO as GPIO
import asyncio
import Adafruit_DHT
from subprocess import call 
from picamera import PiCamera, Color


#DHT declareren
dht_sensor = Adafruit_DHT.DHT11
gpio = 17 #GPIO voor dht sensor

#PIR declareren
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir_sensor = 26 #GPIO voor pir sensor
GPIO.setup(pir_sensor, GPIO.IN, GPIO.PUD_DOWN) #voor ruis weg te werken
current_state = 0

#Toegang token voor discord server
TOKEN = 'TOKEN'
description = '''raspberry in Python'''
bot = commands.Bot(command_prefix='?', description=description)
camera = PiCamera()
def convert_video(file_h264, file_mp4):
    # Record a 3 seconds video.
    camera.start_recording(file_h264)
    time.sleep(3)
    camera.stop_recording()
    # Convert the h264 format to the mp4 format.
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell=True)

#Stuurt "motion detected" bij beweging
async def motionDetection():
    await bot.wait_until_ready()
    channel = bot.get_channel(823209053072523287) # replace with channel ID that you want to send to
    msg_sent = False

    while True:
        try:
            time.sleep(0.1)
            current_state = GPIO.input(pir_sensor)
            if current_state == 1:
                if not msg_sent:
                    await channel.send('Motion Detected')
                    convert_video('/home/pi/Desktop/IOT_Workshop/video.h264', '/home/pi/Desktop/IOT_Workshop/video.mp4')
                    await channel.send(file=discord.File('/home/pi/Desktop/IOT_Workshop/video.mp4'))

                    msg_sent = True
                else:
                    msg_sent = False
                #print("GPIO pin %s is %s" % (pir_sensor, current_state)) # motion detected
                time.sleep(4) # wait 4 seconds for PIR to reset.
        except KeyboardInterrupt:
            GPIO.cleanup()
        await asyncio.sleep(1)

@bot.command()
async def foto(ctx):
    """Bij dit commando wordt er een foto gemaakt en doorgestuurd."""
    camera.capture('/home/pi/Desktop/IOT_Workshop/image.jpg')
    await ctx.send(file=discord.File('/home/pi/Desktop/IOT_Workshop/image.jpg'))
    
@bot.command()
async def video(ctx):
    """Bij dit commando wordt er een video van 3 seconden gemaakt en doorgestuurd."""
    convert_video('/home/pi/Desktop/IOT_Workshop/video.h264', '/home/pi/Desktop/IOT_Workshop/video.mp4')
    await ctx.send(file=discord.File('/home/pi/Desktop/IOT_Workshop/video.mp4'))

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
    #await ctx.send(file=discord.File('video.mp4'))
    await ctx.send("hello lord jesse")

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
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, gpio)
    # Reading the DHT11 is very sensitive to timings and occasionally
    # the Pi might fail to get a valid reading. So check if readings are valid.
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        await ctx.send("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print('Ai, er ging iets mis bij het uitvoeren van de meting. Probeer het even opnieuw.')

bot.loop.create_task(motionDetection())
bot.run(TOKEN)
