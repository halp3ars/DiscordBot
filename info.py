import discord
import datetime
from discord.embeds import Embed, EmptyEmbed
from discord.ext import commands
from discord import client

@client.command()
async def info(ctx):
    embed = discord.Embed(title= "Information about " + ctx.author.name + "#" + ctx.author.discriminator,colour = 0xfcba03 ) 
    embed.set_thumbnail(url = ctx.author.avatar_url)
    embed.add_field(name = "Join discord ", value = ctx.author.created_at.strftime("%m.%d.%Y" ), inline = False)
    embed.add_field(name = "Join server ", value = ctx.author.joined_at.strftime("%m.%d.%Y" ), inline = False)
    embed.add_field(name = "Server nickname", value = ctx.author.display_name, inline = False)
    embed.add_field(name = "Discord nickname", value = ctx.author.name, inline=False,)
    embed.add_field(name = "User ID", value = ctx.author.id, inline=False,)
    roles = ctx.author.roles
    role_names = []
    for role in roles:
        role_names.append(role.name)
    del role_names[0] 
    roles_names = map(( lambda x: '@' + x), role_names)
    embed.add_field(name = "Roles ", value = ",".join(roles_names) , inline=False,)
    now = datetime.datetime.utcnow()
    id = str(ctx.author.id)
    time_string = now.strftime(" %m.%d.%Y %H:%M")
    embed.set_footer(text= time_string + " Requested by " + ctx.author.name + "#" + ctx.author.discriminator + " | "  + id ,icon_url="https://png.pngtree.com/png-vector/20190118/ourmid/pngtree-vector-clock-icon-png-image_323861.jpg")
    await ctx.send(embed=embed)
