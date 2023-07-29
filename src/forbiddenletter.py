from helper.usefulcomponents import Components

# forbidden letter checker
def forbiddenletter(reddit, username):
    forbiddencount = 0
    if username != "":
        for comment in reddit.redditor(username).comments.new(limit=None):
            forbiddencount = forbiddencount + comment.body.count("g")
        replyText = f'u/{username} has said the forbidden letter **{forbiddencount}** times.\n\n*****\n\n^(psst, if theres a problem, report it) [^(here)](https://github.com/neeeerrd/h-bot10000/issues)'
    else:
        replyText = "you need a username to check."
    return replyText
