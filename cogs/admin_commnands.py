import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.core import check, command
from discord_components import DiscordComponents, ComponentsBot, Button, client, component, interaction


class admin(commands.Cog):
    
    def __init__(self,client):
        self.client = client
       
    # Events 
    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(commands)

    
    # Commands 
    @commands.command()
    async def admin(self, ctx):
            await ctx.send(
                "This is admin panel",
                components = [
                    Button(label = "BAN!",style=component.ButtonStyle.red, custom_id="btnBan"),
                    Button(label = "KICK!",style= component.ButtonStyle.green,custom_id="btnKick")
                ]
            )
            interaction = await commands.wait_for("button_click", check = lambda i: i.custom_id == "button1")
            await interaction.send(content = "Button clicked!")

             

def setup(client):
    client.add_cog(admin(client))
