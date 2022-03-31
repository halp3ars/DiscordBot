from email import message
from http import client
import discord
from discord.ext import commands
import discord.embeds
import datetime

import datetime

from numpy import delete

class admin(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass in all requirements") # Part which check that commands have all arguments  
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissons for this") # Part which check the permissons for do command

    #Commands 

    #Ban command 
    @commands.command(name= "ban")
    @commands.guild_only()
    @commands.has_permissions(ban_members= True) #checking permissons (ban)
    async def ban_command(self,ctx, member : discord.Member = None, * , reason = None,delete_message_days=1):
        embed = discord.Embed(title = "Ban info")
        embed.add_field(name= f"{member} has been banned", value= datetime.datetime.utcfromtimestamp.strftime(" %m.%d.%Y %H:%M"))
        embed.set_footer(name= "Admin", value= f"Banned by {ctx.author.name} # {ctx.author.discriminator}")
        await member.ban(reason = reason)
        await ctx.send(embed=embed)

    #Unban command 
    @commands.command(name='unban')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)#checking permissons (ban)
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user}")


    #Kick command 
    @commands.command(name= "kick")
    @commands.guild_only()
    @commands.has_permissions(kick_members = True)#checking permissons (kick)
    async def kick_command(self,ctx, member: discord.Member = None, * , reason = None):
        await member.kick(reason = reason)
        await ctx.send(f"{member} have been kicked | Reason - {reason}")

    #Clear command
    @commands.command(name= "clear")
    @commands.guild_only()
    @commands.has_permissions(manage_messages= True)
    async def clear_chat(self,ctx,amount = 5):
        await ctx.channel.purge(limit = amount)
        await ctx.send("Message has been cleared")

    
       
def setup(client):
    client.add_cog(admin(client))
