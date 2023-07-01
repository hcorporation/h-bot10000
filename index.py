import praw
import time
import os
from dotenv import load_dotenv
import random

load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("ID"),
    client_secret=os.getenv("SECRET"),
    user_agent="python:h-bot10000:v0.0.1 (by /u/neeeerrrdd)",
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD")
)
def run():
  reply_authors = []
  submissions = reddit.subreddit("theletterh").new(limit=2)
  for submission in submissions:
    for tlc in submission.comments:
      for reply in tlc.replies:
        reply_authors.append(reply.author)
      if tlc.author == "h-bot9000" and "h-bot10000" not in reply_authors:   
        prob = random.randint(0,100000)
        prob2 = random.randint(0,10000000000)
        if prob == 1 & prob2 != 1:
          tlc.reply("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        elif prob == 1 & prob2 == 1:
          tlc.reply("e (tHere is a one in like a bajillion cHance that i reply witH e. if you see tHis, consider it qood luck)")
        else:
          tlc.reply("h")
        reply_authors = []
      elif "h-bot10000" in reply_authors:
        reply_authors = []
  time.sleep(60)
  run()

run()