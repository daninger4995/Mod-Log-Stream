import config

import praw

reddit = praw.Reddit(username = config.username,password = config.password,client_id = config.id,client_secret = config.secret,user_agent = config.user_agent)
subreddit = reddit.subreddit(config.sub)

for log in reddit.subreddit("mod").mod.log(limit=5):
    if log.mod in config.mods:
        print("Mod: {}, Action: {}, Link: {}".format(log.mod, log.action, log.target_permalink))

subreddit = reddit.subreddit(config.sub)