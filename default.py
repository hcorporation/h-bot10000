from src.defaultreplier import defaultreplier
from helper.oauthvalidater import validater
from helper.reddit import reddit

validater()
defaultreplier(reddit)