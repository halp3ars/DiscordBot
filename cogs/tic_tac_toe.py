import discord
from discord.ext import commands 


class Mini_Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events


    #Commands
def setup(client):
    client.add_cog(Mini_Games(client)) 