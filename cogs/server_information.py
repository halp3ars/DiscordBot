import datetime
import discord
from discord.ext import commands
from discord.ext.commands import context
from discord.ext.commands.core import command
from discord import guild

class Serverinfo(commands.Cog):


    def __init__(self,client):
        self.client = client

    #Events 
        
    #Commands
    @commands.command(name="server-info")
    async def server_information(self, ctx):
        embed = discord.Embed(title = "Information about" + guild.name + guild.id)
        embed.set_thumbnail(url = guild.icon_url)
        embed.add_field(name= "Categories", value= guild.categories)
        embed.add_field(name= "Rules", value= guild.rules_channel)
        embed.add_field(name= "Date of server creation",value= guild.created_at, inline= False)
        embed.add_field(name= "Owner information" + guild.owener + guild.owener_id)
        time_string = datetime.datetime.utcfromtimestamp.strftime(" %m.%d.%Y %H:%M")
        embed.set_footer(text= time_string + " Requested by " + ctx.author.name + "#" + ctx.author.discriminator + " | "  + id ,icon_url="https://png.pngtree.com/png-vector/20190118/ourmid/pngtree-vector-clock-icon-png-image_323861.jpg")
        await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(Serverinfo(client))