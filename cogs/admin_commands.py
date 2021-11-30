import inspect
import discord
from discord import guild
from discord.ext import commands
from discord.ext.commands.core import has_permissions
from discord.ext.commands.errors import CommandNotFound, NoEntryPointError 
from discord_components import DiscordComponents, ComponentsBot, Button
import discord_components

class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(commands)

    @commands.Cog.listener()
    async def on_command_error(ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass in all requirements") # Part which check that commands have all arguments  
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissons for this") # Part which check the permissons for do command

    #Commands

    @commands.command(name= "ban")
    @commands.has_permissions(ban_members= True) 
    async def ban_command(self,ctx, member : discord.Member, * , reason = None):
        await member.ban(reason = reason) # Ban command with checking permissons 
        await ctx.send(f"{member} have benn banned")
    
    @commands.command(name= "unban")
    @commands.has_permissions(administrator = True)
    async def unban_command(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user} have been unbanned sucessfully")
            return
    
    @commands.command(name= "kick")
    @commands.has_permissions(kick_members = True)
    async def kick_command(self, ctx, member: discord.Member, *, reason = None):
            await member.kick(reason = reason)
            await ctx.send(f"{member} have been kicked")

def setup(client):
    client.add_cog(admin(client))