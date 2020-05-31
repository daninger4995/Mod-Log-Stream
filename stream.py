import discord
import config
import praw
from discord.ext import commands
import json
import datetime


class Reddit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(username = config.username,password = config.password,client_id = config.id,client_secret = config.secret,user_agent = config.user_agent)
        self.bot.loop.create_task(self.get_log())
        self.channel_id = config.channel_id
        self.subreddit = config.sub
        self.timer = 5

    bot = discord.Client()

    @bot.event
    async def on_ready():
        activity = discord.Game(name="Snitchin on you fools yeet yeet", type=3)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        print("Bot is ready")

    async def get_log(self):
        await self.bot.wait_until_ready()
        channel=self.bot.get_channel(config.channel_id)

        while True:
            subreddit = self.reddit.subreddit(self.subreddit)
            for log in self.reddit.subreddit("mod").mod.stream.log(skip_existing=True):
                if log.mod.name in config.name and log.action in config.actiontype:
                    embed = discord.Embed(title="New Mod Action", colour=discord.Colour(0x78df01),
                                        url='https://www.old.reddit.com/{target_permalink}', description="Action Type:{log.action}",
                                        timestamp=datetime.datetime.utcfromtimestamp(1590887053))

                    embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
                    embed.set_author(name="log.mod", url="https://discordapp.com",
                                    icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png")
                    embed.set_footer(text="Contact daninger4995 for any questions")
                    embed = discord.Embed(title=f"{log.action}", description=f"Moderator: /u/{log.mod}", color=0xeee657,)

                    embed.add_field(name="Permalink", value="https://www.reddit.com/r/{log.target_permalink}")
                    embed.add_field(name="OP Username", value=log.target_author)
                    channel = self.bot.get_channel(self.channel_id)
                    await channel.send(embed=embed)

bot = commands.Bot(command_prefix='!', owner_id=config.owner_id)

# Add the cog thingy
bot.add_cog(Reddit(bot))
bot.run(config.discord_id)