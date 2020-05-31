from discord.ext import commands
from stream import Reddit
import config

# Create the bot
bot = commands.Bot(command_prefix='!', owner_id=config.owner_id)

# Add the cog thingy
bot.add_cog(Reddit(bot))

# Run the bot
bot.run(config.discord_id)


