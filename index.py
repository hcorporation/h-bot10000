import praw
import time
import os
from dotenv import load_dotenv

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
  try:
    for submission in reddit.subreddit("theletterh").stream.submissions():
      for tlc in submission.comments:
        for reply in tlc.replies:
          reply_authors.append(reply.author)
        if tlc.author == "h-bot9000" and "h-bot10000" not in reply_authors:
          print("https://reddit.com/r/theletterh/comments/"+str(submission)+"/comment/"+str(tlc))    
          tlc.reply("h")
          reply_authors = []
          print("sent without error")
        elif "h-bot10000" in reply_authors:
          print("https://reddit.com/r/theletterh/comments/"+str(submission)+"/comment/"+str(tlc))
          reply_authors = []
          print("already sent reply")
  except:
    print("rate limited D: waiting one hour")
    time.sleep(3600)
    run()

run()