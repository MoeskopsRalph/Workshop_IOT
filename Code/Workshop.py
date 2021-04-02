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

#Toegang token voor discord server
TOKEN = 'TOKEN'
description = '''IOT Workshop - Discord Bot'''
bot = commands.Bot(command_prefix='?', description=description)

#DHT declareren
dht_sensor = Adafruit_DHT.DHT11
gpio = 18 #GPIO voor dht sensor

#PIR declareren
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir_sensor = 24 #GPIO voor pir sensor
GPIO.setup(pir_sensor, GPIO.IN, GPIO.PUD_DOWN) #voor ruis weg te werken
current_state = 0

#RELAIS declareren
gpio2 = 21
gesloten = 0
GPIO.setup(gpio2,GPIO.OUT)

#CAMERA declaren + functie
camera = PiCamera()
camera.resolution = (640,480)
def convert_video(file_h264, file_mp4):
    # Opnemen 3 seconde video
    camera.start_recording(file_h264)
    time.sleep(3)
    camera.stop_recording()
    # Omzetten h264 formaat naa mp4 formaat
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
                    commando = "rm " +"/home/pi/Desktop/IOT_Workshop/video.mp4"
                    call([commando], shell=True)
                    msg_sent = True
                else:
                    msg_sent = False
                #print("GPIO pin %s is %s" % (pir_sensor, current_state)) # motion detected
                time.sleep(4) # wait 4 seconds for PIR to reset.
        except KeyboardInterrupt:
            GPIO.cleanup()
        await asyncio.sleep(1)

@bot.event
async def on_ready():
    print('Bot opgestart en ingelogd als:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

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
    commando = "rm " +"/home/pi/Desktop/IOT_Workshop/video.mp4"
    call([commando], shell=True)

@bot.command()
async def meting(ctx):
    """Bij dit commando wordt de temperatuur en luchtvochtigheid opgemeten."""
    await ctx.send('De temperatuur en luchtvochtigheid worden gemeten, even geduld. De resultaten worden zodadelijk verstuurd')
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, gpio)
    if humidity is not None and temperature is not None:
        await ctx.send('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        await ctx.send('Ai, er ging iets mis bij het uitvoeren van de meting. Probeer het even opnieuw.')

@bot.command()
async def schakelaar(ctx, switch : str):
    """Bij dit commando wordt de relais aan en uit gezet."""
    if switch == 'Gesloten' and gesloten == 0:
        GPIO.output(gpio2,GPIO.HIGH)
        gesloten = 1
        print('RELAIS Gesloten')
        await ctx.send('RELAIS Gesloten')
    elif switch == 'Open' and gesloten == 1:
        GPIO.output(gpio2,GPIO.LOW)
        gesloten = 0
        print('RELAIS Open')
        await ctx.send("RELAIS Open")
    elif switch == 'Gesloten' and gesloten == 1:
        print('RELAIS Is Al Gesloten!')
        await ctx.send("RELAIS Open!")
    elif switch == 'Open' and gesloten == 0:
        print('RELAIS Is Al Open!')
        await ctx.send("RELAIS Is Al Open!")
    else:
        print('Commando niet herkend: gebruik Gesloten/Open')
        await ctx.send('Commando niet herkend: gebruik Gesloten/Open')

bot.loop.create_task(motionDetection())
bot.run(TOKEN)
