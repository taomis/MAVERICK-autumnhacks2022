import discord
from discord import app_commands
from discord.ext import commands

guild_id = 486327698751488016

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=discord.Object(id=guild_id))
        await self.tree.sync(guild=discord.Object(id=guild_id))

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.tree.command()
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        colour = discord.Colour.green(),
        title = "Bot Commands",
        description = ""
    )
    #embed.set_author(name = "MAVERICK", icon_url = "image url")
    #embed.set_image(url = "image url")
    #embed.set_thumbnail(url = "https://media.discordapp.net/attachments/967987262048567306/1018742994310008872/unknown.png")
    embed.add_field(name = "setrem *time_zone* *time*", value = "0")
    embed.add_field(name = "CALc **", value = "0")
    #embed.footer(text = "This is a footer")

    await interaction.response.send_message(embed = embed, ephemeral=True)
    

#@client.tree.command()
async def setrem():
    pass

#@client.tree.command()
async def CALc():
    pass


client.run('MTAxODM0ODQzNTYwNDI0MjQ4NA.GW-fey.pN8W-_7mNo18fK_JB85l3L8qQps_3ua-NtCWNs')