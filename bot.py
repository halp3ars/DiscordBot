import discord
import os
from discord.ext import commands
from discord import client

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@client.command(hidden = True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command(hidden = True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run("")
