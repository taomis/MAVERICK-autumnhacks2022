import discord, dependencies as d
from discord import app_commands
from discord.ext import commands

guild_id = 0 # change it to your server's id

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
    embed.add_field(name = "CALc **", value = "0")
    #embed.footer(text = "This is a footer")

    await interaction.response.send_message(embed = embed, ephemeral=True)
    
@client.tree.command()
@app_commands.rename(weight='weight')
@app_commands.rename(height='height')
@app_commands.rename(age='age')
@app_commands.rename(selection='selection')
async def exercise(interaction: discord.Interaction, weight: str, height: str, age: str, selection: str):
    await interaction.response.send_message('The amount of calories you need is to maintain Weight is ' + str(d.type_of_exercise(weight, height, age, selection)))

@app_commands.rename(weight='weight')
@app_commands.rename(height='height')
@client.tree.command()
async def bmi(interaction: discord.Interaction, weight: str, height: str):
    await interaction.response.send_message(str('Your body mass index is ' + str(d.bmi(weight, height)) + '\n' + str(d.bmi_2(weight, height))))


client.run('token')
