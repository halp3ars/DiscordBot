import discord
from discord import channel
from discord.ext import commands
from discord.flags import Intents
from discord.utils import get


class Events(commands.Cog):

    def __init__(self,client):
        self.client = client

    #Events 

    @commands.Cog.listener()
    async def on_member_join(self,member):
        await member.send("Hey i hope you will like our community <3")

    @commands.Cog.listener()
    async def on_ready(self):
        print ("Bot load from the server")
        await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.streaming,name= " on YouTube",url = "https://www.youtube.com/watch?v=PY8f1Z3nARo&ab_channel=JomaTech", platform = "YouTube"))

    @commands.Cog.listener()
    async def on_member_join(self,member):
        role = get(member.guild.roles, id=866612722971836427)
        await member.add_roles(role)

    #Commands 

def setup(client):
    client.add_cog(Events(client))