from src.defaultreplier import defaultreplier
from helper.oauthvalidater import validater
from helper.reddit import reddit
import time

validater()
def replier():
    try:
        defaultreplier(reddit)
    except:
        time.sleep(60)
        replier()
replier()