from helper.usefulcomponents import Components
from src.aireplier import ai
from src.forbiddenletter import forbiddenletter
from src.topposts import topposts

def mentionuser(reddit, key):
    components = Components(reddit)
    new_mentions = components.new_mentions()
    error_reply = "an error occurred. doesn't seem right? report it [here](https://github.com/neeeerrd/h-bot10000)"
    for mention in new_mentions:
        if "u/h-bot10000 !forbiddenLetter" in mention.body:
            forbiddencount = 0
            username = mention.body.replace("/u/h-bot10000 !forbiddenLetter ", "")
            username = username.replace("/u/", "")
            try:
                reply = forbiddenletter(reddit, username)
                mention.reply(reply)
            except:
                mention.reply(error_reply)
        elif "!betaAi" in mention.body:    
            prompt = mention.body.replace("/u/h-bot10000 !betaAi ", "")
            try:
                reply = ai(prompt, key, mention.author)
                mention.reply(reply)
            except:
                mention.reply(error_reply)
        elif "u/h-bot10000 !topPosts" in mention.body:
            range = mention.body.replace("/u/h-bot10000 !topPosts ", "")
            try:
                reply = topposts(reddit, range)
                mention.reply(reply)
            except:
                mention.reply(error_reply)
        elif "u/h-bot10000 !copypasta" in mention.body:
            file = open("assets/copypasta.txt")
            mention.reply(file.read())
        else:
            mention.reply("h")
