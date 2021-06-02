import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
	channel = client.get_channel(849758362186153984)
	
	await channel.send("Hello there!")

with open("token.txt", "r") as token:
	Start_Bot = token.read()
		
client.run(Start_Bot)