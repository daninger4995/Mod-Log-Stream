import discord
import config
import praw
import json

class Reddit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(username = config.username,password = config.password,client_id = config.id,client_secret = config.secret,user_agent = config.user_agent)
        self.bot.loop.create_task(self.get_log())
        self.channel_id = config.channel_id
        self.subreddit = config.sub
        self.timer = 5

def main():

    bot = discord.Client()

    @bot.event
    async def on_ready():
        activity = discord.Game(name="Snitchin on you fools yeet yeet", type=3)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        print("Bot is ready")

    async def get_log(self):
        await self.bot.wait_until_ready()

        while True:
            # Get the id of the last submission posted to discord
            with open('log.json', 'r') as file:
                latest_log_id = json.loads(file.read())['log.id']

            # If the submission is new, send it
            subreddit = self.reddit.subreddit(self.subreddit)
            for log in reddit.subreddit("mod").mod.log(limit=1):
                if log.id != latest_log_id and submission != None:
                    self.store_latest_log_id(log.id)
                    await self.post_log(log)

    async def post_log(self, log)
        channel = self.bot.get_channel(self.channel_id)

        embed = self.create_embed(log)
        await channel.send(embed=embed)

    # Put
    def store_latest_log_id(self, log_id):
        with open('log.json', 'w') as file:
                    file.write(json.dumps({'log_id': log.id}))

    # Creates an embed of the reddit submission
    # Alters the embed based on the tag parameter
    def create_embed(self, log):
        # All embed types share the same color, title, timestamp,
        # author, and thumbnail, data will hold all the embed options
        data = {
            'color': 0x7fff00,
            'title': {log.action},
            'url': {'url': f'https://www.old.reddit.com{log.target_permalink},
            'author': {'Mod': f'/u/{log.mod}'},
            'timestamp': datetime.datetime.utcnow().isoformat(),
        }
    bot.run(config.discord_id)

main()