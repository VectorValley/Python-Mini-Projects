from urllib import response
import discord
from discord import File
from discord.utils import get
from discord.ext import commands
import os
import random
import requests
import json
from dotenv import load_dotenv
from easy_pil import Editor, load_image_async, Font
from list_data import *


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

load_dotenv()
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    author = json_data[0]['a']
    quote_content = f"{quote}\n    -{author}"
    return(quote_content)


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Orbit'))
  print('Bot has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content.lower()
  
  if message.author == client.user:
    return


    # Greeting Section
  if msg.startswith('$hi'):
    await message.channel.send('hello sir! How can I help you')
  
  
     
  if any(word in msg for word in bad_word):
    await message.channel.send(f"{random.choice(worning)}")  
    
        
  if msg.startswith('?quote'):
    await message.channel.send(get_quote())



@client.event
async def on_member_join(member):
    guild = client.get_guild(952175289209851956) 
    welcome_channel = client.get_channel(952175290082275329) 
    # await welcome_channel.send(f'Welcome to the {guild.name}, {member.mention} !  :partying_face:\n\n You are the {w} member of {guild.name}')
    # await member.send(f'We are glad to have you in the {guild.name} Discord Server, {member.name} !  :partying_face:\n\nPlease go through the #communityi-rules & be a part of {guild.name}\n\nAnd Do not forget to Subscribe our YouTube Channel')

    pos = sum(m.joined_at < member.joined_at for m in member.guild.members if m.joined_at is not None)

    if pos == 1:
      te = "st"
    elif pos == 2:
      te = "nd"
    elif pos == 3:
      te = "rd"
    else: te = "th"

    background = Editor("bg.jpg")
    profile_image = await load_image_async(str(member.avatar_url))

    profile = Editor(profile_image).resize((150, 150)).circle_image()
    poppins = Font.poppins(size=50, variant="bold")

    poppins_small = Font.poppins(size=20, variant="light")

    background.paste(profile, (325, 90))
    background.ellipse((325, 90), 150, 150, outline="gold", stroke_width=4)

    background.text((400, 260), f"WELCOME TO {member.guild.name}", color="white", font=poppins, align="center")
    background.text((400, 325), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
    background.text((400, 360), f"You Are The {pos}{te} Member", color="#0BE7F5", font=poppins_small, align="center")

    file = File(fp=background.image_bytes, filename="wlcbg.jpg")

    #if you want to message more message then you can add like this
    await welcome_channel.send(f"Heya {member.mention}! Welcome To **{member.guild.name} For More Information Go To <#885152158599770183>**")

    #for sending the card
    await welcome_channel.send(file=file)

@client.event
async def on_member_remove(member):
  guild = client.get_guild(952175289209851956) 
  welcome_channel = guild.get_channel(952175290082275329)

  await welcome_channel.send(f"{member.name} Has Left The server, We are going to miss you :( ")


client.run(os.getenv("TOKEN"))