import os
import praw
from dotenv import load_dotenv

# provides the reddit() function used for getting replies, etc. also reads authentication details.

load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("ID"),
    client_secret=os.getenv("SECRET"),
    user_agent="python:h-bot10000:v1.0.0 (by u/neeeerrrdd)",
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD")
)
