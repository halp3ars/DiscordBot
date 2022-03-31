import discord
import datetime
from discord.ext import commands



class serverinf(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    
    # Events  

    # Commands 
    @commands.command()
    @commands.guild_only()
    async def server(self ,ctx):
        embed = discord.Embed(title="Server Information",color = discord.Colour.random())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name ="Server name " ,value= ctx.guild.name)
        embed.add_field(name ="ID" ,value= ctx.guild.id )
        embed.add_field(name = "Owner", value= f"{ctx.guild.owner} id {ctx.guild.owner_id} " , inline= False)
        roles = ctx.guild.roles
        role_names = []
        for role in roles:
            role_names.append(role.name)
        del role_names[0] 
        roles_names = map(( lambda x: '@' + x), role_names)
        embed.add_field(name = "Roles ", value = ",".join(roles_names) , inline=False,)
        embed.add_field(name= "Member Count", value = f"{ctx.guild.member_count}")
        time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        embed.set_footer(text = f"{time} Requsted by {ctx.author.name}#{ctx.author.discriminator}",icon_url="https://png.pngtree.com/png-vector/20190118/ourmid/pngtree-vector-clock-icon-png-image_323861.jpg")
        
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(serverinf(client))


    