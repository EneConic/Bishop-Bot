import discord
from discord.ext import commands
import os
import random

client = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
	channel = client.get_channel(849758362186153984)
	
	await channel.send("Hello there!\n\nWhat can I help you with today?")

@client.command(hidden=True)
async def load(ctx, extension):

    client.load_extension(f'cogs.{extension}')
    print(f"Cog {extension} is loaded")

@client.command(hidden=True)
async def unload(ctx, extension):

    client.unload_extension(f'cogs.{extension}')
    print(f"Cog {extension} is unloaded")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') 

with open("token.txt", "r") as token:
	Start_Bot = token.read()
		
client.run(Start_Bot)