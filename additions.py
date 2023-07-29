from helper.reddit import reddit
from helper.mentions import mentionuser
import time
from dotenv import load_dotenv
import os

load_dotenv()

def replier():
    key = os.getenv("OPENAI_KEY") 
    try:
        mentionuser(reddit, key)
    except:
        time.sleep(60)
        replier()

replier()
