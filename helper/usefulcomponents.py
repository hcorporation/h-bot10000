import praw

# components for readable code

class Components:
    def __init__(self, reddit):
        self = self
        self.reddit = reddit
    def new_comments(self):
        comments = self.reddit.redditor("h-bot9000").stream.comments(skip_existing=True)
        return comments
    def new_mentions(self):
        mentions = self.reddit.inbox.mentions
        return praw.models.util.stream_generator(mentions, skip_existing=True)
    def top_posts(self, range):
        return self.reddit.subreddit("theletterh").top(limit=5, time_filter=range)
