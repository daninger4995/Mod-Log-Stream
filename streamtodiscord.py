import discord

def main():
	client.run(config.discord_id)

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Snitchin on you fools yeetyeet))

