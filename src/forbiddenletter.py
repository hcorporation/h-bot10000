from helper.usefulcomponents import Components

# forbidden letter checker
def forbiddenletter(reddit):
    def replier(mention, forbiddencount, username):
        if username != "":
            for comment in reddit.redditor(username).comments.new(limit=None):
                forbiddencount = forbiddencount + comment.body.count("g")
            mention.reply(f'u/{username} has said the forbidden letter **{forbiddencount}** times.\n\n*****\n\n^(psst, if theres a problem, report it) [^(here)](https://github.com/neeeerrd/h-bot10000/issues)')
        else:
            mention.reply("you need a username to check.")
        mention.mark_read()

    components = Components(reddit)
    new_mentions = components.new_mentions()
    for mention in new_mentions:
        if "u/h-bot10000 !forbiddenLetter" in mention.body:
            forbiddencount = 0
            if "/u/h-bot10000" in mention.body:
                username = mention.body.replace("/u/h-bot10000 !forbiddenLetter ", "")
            elif "u/h-bot10000" in mention.body:
                username = mention.body.replace("u/h-bot10000 !forbiddenLetter ", "")
            if "/u/" in username:
                username = username.replace("/u/", "")
            elif "u/" in username:
                username = username.replace("u/", "")
            try:
                replier(mention, forbiddencount, username)
            except:
                mention.reply("an error occurred. doesn't seem right? report it [here](https://github.com/neeeerrd/h-bot10000/issues)")
        else:
            mention.reply("h")
