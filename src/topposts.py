from helper.usefulcomponents import Components

def topposts(reddit, range):
    components = Components(reddit)
    posts = components.top_posts(range)
    replyText = ""
    for post in posts:
        replyText += "\n\n https://www.reddit.com" + post.permalink
    replyText += "\n\n******\n\n ^(does something look wrong? report it) [^(here)](https://github.com/neeeerrd/h-bot10000/issues)"
    return replyText