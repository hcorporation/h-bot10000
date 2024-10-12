import os
import random
import praw
from dotenv import load_dotenv

load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("ID"),
    client_secret=os.getenv("SECRET"),
    user_agent="python:h-bot10000:v24.04 (by /u/neeeerrrdd2)",
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD")
)

while True:
    try:
        for post in reddit.subreddit("theletterh").stream.submissions(skip_existing=True):
            number = random.choice([0,1])
            if number == 0:
                post.reply("h")
            else:
                post.reply("H")
    except Exception as e:
        print(e)
        if "invalid_grant" in str(e):
            print("log out and log in again on reddit.com to rectify this issue.")
            break
        else:
            continue
