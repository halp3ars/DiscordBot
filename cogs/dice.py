from email import message
import discord
from discord.ext import commands
import random


class Mini_Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events

    #Commands
    @commands.command(name= "dice")
    async def roll_dice(self,ctx):
        random_die= random.randint(1,6)
        if random_die == 1:
            random_die = str("https://www.freeiconspng.com/uploads/dice-png-8.png")
        elif random_die == 2:
            random_die = str("https://www.freeiconspng.com/uploads/dice-png-24.png")    
        elif random_die == 3:
            random_die = str("https://www.freeiconspng.com/uploads/dice-png-33.png") 
        elif random_die == 4:
            random_die = str("https://www.freeiconspng.com/uploads/dice-png-9.png") 
        elif random_die == 5:
            random_die = str("https://www.freeiconspng.com/uploads/dice-png-13.png") 
        elif random_die == 6:
            random_die = str("https://www.freeiconspng.com/uploads/dice-png-32.png") 
        await ctx.send(f"{random_die}")    



def setup(client):
    client.add_cog(Mini_Games(client)) 