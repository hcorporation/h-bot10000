from helper.reddit import reddit
from src.forbiddenletter import forbiddenletter
import time

def replier():
    try:
        forbiddenletter(reddit)
    except:
        time.sleep(60)
        replier()

replier()
