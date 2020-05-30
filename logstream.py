import config

import praw

reddit = praw.Reddit(username = config.username,password = config.password,client_id = config.id,client_secret = config.secret,user_agent = config.user_agent)
subreddit = reddit.subreddit(config.sub)


for log in reddit.subreddit("mod").mod.log(limit=1000):
    if log.mod.name in config.name and if
        print("Mod: {}, Action: {}, Link: {}".format(log.mod, log.action, log.target_permalink))

    if log.mod.name not in config.name:
        continue

subreddit = reddit.subreddit(config.sub)