from helper.usefulcomponents import Components

# forbidden letter checker
def forbiddenletter(reddit):
    def replier(mention, forbiddencount, username):
        if username != "":
            for comment in reddit.redditor(username).comments.new(limit=None):
                forbiddencount = forbiddencount + comment.body.count("g")
            mention.reply(f'u/{username} has said the forbidden letter **{forbiddencount}** times.\n\n*****\n\n^(psst, if theres a problem, report it) [^here](https://github.com/neeeerrd/h-bot10000/issues)')
        else:
            mention.reply("you need a username to check.")
        mention.mark_read()

    components = Components(reddit)
    new_mentions = components.new_mentions()
    for mention in new_mentions:
        if mention.new:
            if "u/h-bot10000 !forbiddenLetter u/" in mention.body:
                forbiddencount = 0
                username = mention.body.replace("u/h-bot10000 !forbiddenLetter u/","")
                if "/" in username:
                    trueusername = username.replace("/","")
                try:
                    replier(mention, forbiddencount, trueusername)
                except:
                    mention.reply("an error occurred. doesn't seem right? report it [here](https://github.com/neeeerrd/h-bot10000/issues)")
                    mention.mark_read()
            elif "u/h-bot10000 !forbiddenLetter /u/" in mention.body:
                forbiddencount = 0
                username = mention.body.replace("u/h-bot10000 !forbiddenLetter /u/","")
                if "/" in username:
                    trueusername = username.replace("/","")
                try:
                    replier(mention,forbiddencount,trueusername)
                except:
                    mention.reply("an error occurred. doesn't seem right? report it [here](https://github.com/neeeerrd/h-bot10000/issues)")
                    mention.mark_read()
            else:
                mention.reply("h")
                mention.mark_read()
